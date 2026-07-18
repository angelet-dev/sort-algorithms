import textwrap
import numpy as np
import os
from datetime import datetime
import logging


def form_results(
    sort_func_list: list,
    list_of_times: list,
    builtin_sort_times: list,
    array_size: int,
    num_workers: int,
    iterations: int,
    sort_tag: str,
    DTYPE: str,
) -> str:

    form_text = []
    builtin_mean_time = np.mean(builtin_sort_times)

    title = textwrap.dedent(f"""
    =========================================================================
                                    RESULTS                  
    =========================================================================
    DTYPE = {DTYPE}  
    Mean time of {sort_tag} = {builtin_mean_time:.6f} sec                       
    =========================================================================
    """).strip()

    form_text.append(title)

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
        form_text.append(report)

    return "\n".join(form_text)


def save_results_to_file(
    formatted_text: str, save_to_file: bool, prefix: str = "bench"
) -> None:

    if not save_to_file:
        return None

    try:
        os.makedirs("reports", exist_ok=True)

        time = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_path = f"reports/{prefix}_{time}.txt"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(formatted_text)

        return None

    except Exception as e:
        logging.error(f"File write error {type(e).__name__}: {e}")
        return None
