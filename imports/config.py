import pandas as pd

def get_number_of_samples():
    """
    Get the number of samples defined in samples.tsv.
    """
    config_samples = pd.read_csv("config/samples.tsv", sep="\t")
    ans = len(config_samples["sample_id"])
    return ans
