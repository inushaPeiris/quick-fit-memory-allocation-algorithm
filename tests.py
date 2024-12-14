import unittest
from quick_fit import QuickFit

class TestQuickFit(unittest.TestCase):
    def setUp(self):
        """Set up a QuickFit allocator before each test."""
        self.block_sizes = [64, 128, 256]
        self.initial_blocks = 2
        self.allocator = QuickFit(self.block_sizes, self.initial_blocks)

    def test_initial_pool_creation(self):
        """Test that pools are created with correct initial blocks."""
        for size in self.block_sizes:
            self.assertEqual(len(self.allocator.pools[size]), self.initial_blocks)
            self.assertTrue(all(f"Block_{size}_{i}" in self.allocator.pools[size] for i in range(self.initial_blocks)))

    def test_pool_allocation(self):
        """Test allocating from predefined pool sizes."""
        for size in self.block_sizes:
            block = self.allocator.allocate(size)
            self.assertIsNotNone(block)
            self.assertIn(block, [f"Block_{size}_{i}" for i in range(self.initial_blocks)])

    def test_dynamic_allocation(self):
        """Test dynamic allocation for sizes not in predefined pools."""
        # Exhaust all predefined pool blocks
        for size in self.block_sizes:
            for _ in range(self.initial_blocks):
                self.allocator.allocate(size)

        # Allocate a new size to trigger dynamic allocation
        dynamic_block = self.allocator.allocate(512)
        self.assertIn(dynamic_block, self.allocator.dynamic_allocations)

    def test_deallocation(self):
        """Test deallocating blocks back to pools and dynamic allocations."""
        # Allocate and then deallocate a pool block
        for size in self.block_sizes:
            block = self.allocator.allocate(size)
            initial_pool_count = len(self.allocator.pools[size])
            self.allocator.deallocate(block)
            self.assertEqual(len(self.allocator.pools[size]), initial_pool_count + 1)

        # Allocate and deallocate a dynamic block
        dynamic_block = self.allocator.allocate(512)
        self.allocator.deallocate(dynamic_block)
        self.assertNotIn(dynamic_block, self.allocator.dynamic_allocations)

if __name__ == '__main__':
    unittest.main()
