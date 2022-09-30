import os
import geopandas as gpd
import main as mn
import numpy as np

def get_shp_files(basedir, object_type, file_type='.shp'):
    print(f'Initiating with {file_type} file reading over {object_type} type of files.')
    
    final_dir = os.path.join(basedir, object_type)
    
    existing_files = os.listdir(final_dir)
    
    returning_files = {}
    for existing_file in existing_files:

        if file_type in existing_file:

            file_name = existing_file.strip(file_type)
            
            print(f'Found file {file_type}: {file_name}.')
                                            
            path_to_specific_file = os.path.join(final_dir, existing_file)
            returning_files[file_name] = gpd.read_file(path_to_specific_file)
    
    print(f'Done with file seek over {object_type}.')
    return returning_files

    
def get_corr(v1,v2,numeric_performers):
    corr_v = numeric_performers.corr()[v1].sort_values(ascending=False)

    for i in range(len(corr_v)):
        if corr_v.index[i]==v2:
            return(f'{v2} is the **Top {i}** most correlated variable to {v1}. **Correlation: {np.round(corr_v.loc[v2],4)}**')
