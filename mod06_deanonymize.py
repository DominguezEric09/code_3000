import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    merged = anon_df.merge(aux_df, on=["age", "gender", "zip3"])
    merged["anon_id_count"] = merged.groupby("anon_id")["anon_id"].transform("size")
    merged["name_count"] = merged.groupby("name")["name"].transform("size")
    unique_matches = merged[(merged["anon_id_count"] == 1) & (merged["name_count"] == 1)]
    result = unique_matches[["anon_id", "name"]].rename(columns={"name": "matched_name"})
    return result


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    num_matched = len(matches_df)
    num_total = len(anon_df)
    rate = num_matched / num_total
    return rate
