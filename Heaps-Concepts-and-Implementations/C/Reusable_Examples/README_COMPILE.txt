Compile reusable C examples from the C folder:

  gcc heap_helpers.c Reusable_Examples/01_top_k_largest_reusing_helpers.c -o topk
  gcc heap_helpers.c Reusable_Examples/02_connect_sticks_reusing_helpers.c -o sticks

The helper implementation is compiled once and reused by the problem file.
