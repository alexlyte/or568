# -*- coding: utf-8 -*-

#----------------------------------------------------------------------------------------
# get_hit_rate_stats(infile):  gets the threat probabilities in a useful form
#
# infile:                      labels csv file
#
# returns:                     a dataframe of the summary hit probabilities
#
#----------------------------------------------------------------------------------------

def get_hit_rate_stats(infile):
    # pull the labels for a given patient
    df = pd.read_csv(infile)

    # Separate the zone and patient id into a df
    df['Subject'], df['Zone'] = df['Id'].str.split('_',1).str
    df = df[['Subject', 'Zone', 'Probability']]

    # make a df of the sums and counts by zone and calculate hit rate per zone, then sort high to low
    df_summary = df.groupby('Zone')['Probability'].agg(['sum','count'])
    df_summary['Zone'] = df_summary.index
    df_summary['pct'] = df_summary['sum'] / df_summary['count']
    df_summary.sort_values('pct', axis=0, ascending= False, inplace=True)
    
    return df_summary

# unit test -----------------------
#df = get_hit_rate_stats(THREAT_LABELS)
#df.head()