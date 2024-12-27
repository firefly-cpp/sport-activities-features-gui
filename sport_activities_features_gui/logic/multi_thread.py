from sport_activities_features.tcx_manipulation import TCXFile
import pandas as pd
from multiprocessing import Pool, Manager


class MultiThread:
    """This class handles the multi-threading for the TCX file loading."""
    def single_load(self, path_of_file: str) -> pd.DataFrame:
        """This function loads a single TCX file.
        Args:
            path_of_file (str): The path of the file to load.
        """
        try:
            tcx_file = TCXFile()
            tcx_exercise = tcx_file.read_one_file(path_of_file)            
            activity = tcx_file.extract_activity_data(tcx_exercise)
            integral_metrics = tcx_file.extract_integral_metrics(tcx_exercise)
            all_data = activity | integral_metrics
            df = pd.DataFrame(all_data)
            return df
        except:
            return pd.DataFrame

    def _single_load_inner(self, path_of_file: str, data):
        """This internal function loads a single TCX file.
        Args:
            path_of_file (str): The path of the file to load.
            data (list): The list to append the data to.
        """
        try:
            tcx_file = TCXFile()
            tcx_exercise = tcx_file.read_one_file(path_of_file)            
            activity = tcx_file.extract_activity_data(tcx_exercise)
            integral_metrics = tcx_file.extract_integral_metrics(tcx_exercise)
            all_data = activity | integral_metrics
            data.append(all_data)
        except:
            a = 1
            # better error handling

    def bulk_load(self, files: list, num_of_processes: int) -> dict:
        """This function loads multiple TCX files with multithreading.
        Args:
            files (list): The list of files to load.
            num_of_processes (int): The number of processes to use.
        """
        tcx_file = None
        # files = None
        # try:
        #     tcx_file = TCXFile()
        #     files = tcx_file.read_directory(directory_name=directory_path)
        # except:
        #     # better error handling
        #     return None

        with Manager() as manager:
            data = manager.list()
            with Pool(processes=num_of_processes) as pool:
                pool.starmap(self._single_load_inner, [
                             (file, data) for file in files])
                # pool.map(self._single_load_inner, product(files, data, arrError))

            return {
                'data': pd.DataFrame(list(data)),
                'numOfFiles': len(files),
                'numOfFilesNotRead': (len(files) - len(data))
            }
