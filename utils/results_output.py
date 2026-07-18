import textwrap
import numpy as np


def form_results(
    sort_func_list: list,
    list_of_times: list,
    builtin_sort_times: list,
    array_size: int,
    num_workers: int,
    iterations: int,
    sort_tag: str,
) -> None:

    results = textwrap.dedent("""
    =========================================================================
                                    RESULTS                  
    =========================================================================
    """).strip()
    print(results)

    builtin_mean_time = np.mean(builtin_sort_times)

    for i in range(len(sort_func_list)):
        mean_time = np.mean(list_of_times[i])
        min_time = np.min(list_of_times[i])
        max_time = np.max(list_of_times[i])
        ratio = mean_time / builtin_mean_time

        pure_core_time = sum(list_of_times[i]) / num_workers

        report = textwrap.dedent(f"""
        Name of sort algorithm:             {sort_func_list[i].__name__}
        Number of elements in array:        {array_size:,}
        Number of iterations:               {iterations:,}
        Mean time of sort:                  {mean_time:.6f} sec
        Min time of sort:                   {min_time:.6f} sec
        Max time of sort:                   {max_time:.6f} sec
        Pure CPU time per core:             {pure_core_time:.4f} sec
        Number of workers (cores):          {num_workers} 
        In comparison with {sort_tag}: {ratio:.2f}x slower
        =========================================================================
        """).strip()
        print(report)
