from sport_activities_features.tcx_manipulation import TCXFile
from sport_activities_features.hill_identification import HillIdentification
from sport_activities_features.topographic_features import TopographicFeatures

from multiprocessing import Pool, Manager

class MultiThread:
    def __init__(self):
        print("Not implemented")
    
    def single_load(path_of_file: str) -> dict: 
        try:
            tcx_file = TCXFile()
            activity = tcx_file.read_one_file(path_of_file)
            integral_metrics = tcx_file.extract_integral_metrics(path_of_file)
            all_data= activity | integral_metrics
            return all_data
        except:
            # better error handling 
            return None

    def _single_load_inner(path_of_file: str, arr: list): 
        try:
            tcx_file = TCXFile()
            activity = tcx_file.read_one_file(path_of_file)
            integral_metrics = tcx_file.extract_integral_metrics(path_of_file)
            all_data= activity | integral_metrics
            arr.append(all_data)
        except:
            # better error handling
            print("shitty data")
    
    def bulk_load(self, directory_path: str, num_of_processes: int) -> list:
        tcx_file = None
        files = None
        try:
            tcx_file = TCXFile()
            files = tcx_file.read_directory(directory_name=directory_path)
        except:
            # better error handling 
            return None
        with Manager() as manager:
            data = manager.list()
            with Pool(processes=num_of_processes) as pool:
                # this might work i think 
                pool.starmap(self._single_load_inner, [(file, data) for file in files])
            # print(data)
            return list(data)