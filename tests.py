import unittest
from quick_fit import QuickFit

class TestQuickFit(unittest.TestCase):
    def setUp(self):
        self.block_sizes = [64, 128, 256, 512]
        self.initial_blocks = 3
        self.allocator = QuickFit(self.block_sizes, self.initial_blocks)

    def test_allocate_predefined(self):
        block_id = self.allocator.allocate(64)
        self.assertIn(block_id, self.allocator.pools[64])

    def test_allocate_dynamic(self):
        block_id = self.allocator.allocate(300)
        self.assertIn(block_id, self.allocator.dynamic_allocations)

    def test_deallocate_predefined(self):
        block_id = self.allocator.allocate(64)
        self.allocator.deallocate(block_id)
        self.assertIn(block_id, self.allocator.pools[64])

    def test_deallocate_dynamic(self):
        block_id = self.allocator.allocate(300)
        self.allocator.deallocate(block_id)
        self.assertNotIn(block_id, self.allocator.dynamic_allocations)

if __name__ == '__main__':
    unittest.main()
