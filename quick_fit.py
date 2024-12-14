class QuickFit:
    def __init__(self, block_sizes, initial_blocks):
        """
        Initializes memory pools for quick allocation based on the given block sizes.
        :param block_sizes: List of predefined block sizes for memory pools.
        """
        self.pools = {size: [f"Block_{size}_{i}" for i in range(initial_blocks)] for size in block_sizes}
        self.dynamic_allocations = {}

    def allocate(self, size):
        """
        Allocates memory of the requested size.
        :param size: The size of the memory block to allocate.
        :return: The allocated block ID.
        """
        if size in self.pools:
            if self.pools[size]:
                print(f"\nAllocated block of size {size} from pool.")
                return self.pools[size].pop()
            else:
                print(f"\nNo free blocks in pool for size {size}. Allocating dynamically.")
        
        block_id = id(size)
        self.dynamic_allocations[block_id] = size
        print(f"Dynamically allocated block of size {size} with ID {block_id}.")
        return block_id

    def deallocate(self, block_id):
        """
        Deallocates the specified memory block.
        :param block_id: The unique identifier of the memory block to deallocate.
        """
        for size, pool in self.pools.items():
            if block_id in pool:
                pool.append(block_id)
                print(f"\nBlock of size {size} returned to pool.")
                return

        if block_id in self.dynamic_allocations:
            print(f"Dynamically allocated block with ID {block_id} released.")
            del self.dynamic_allocations[block_id]
        else:
            print(f"Invalid block ID: {block_id}")

    def view_pools(self):
        """Displays the status of all memory pools."""
        print("\nMemory Pools Status:")
        for size, pool in self.pools.items():
            print(f"Size {size}: {len(pool)} free blocks")

    def view_dynamic_allocations(self):
        """Displays all dynamic allocations."""
        print("\nDynamic Allocations:")
        for block_id, size in self.dynamic_allocations.items():
            print(f"ID: {block_id}, Size: {size}")
