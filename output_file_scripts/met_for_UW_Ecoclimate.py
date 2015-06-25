# Script to create and export data files for the UWashington Ecoclimate project


import sys
sys.path.append( '/home/greg/current/NMEG_utils/py_modules/' )

import load_nmeg as ld
import transform_nmeg as tr
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ipdb as ipdb

datapath = ('/home/greg/sftp/eddyflux/Ameriflux_files/provisional/')
fileList = os.listdir(datapath)

startyear = 2007
endyear = 2014

# List AF site names in same order
siteNames = [ 'US-Mpj', 'US-Mpg' ]

for i, site in enumerate( siteNames ):
    # For now the data are different in 2007-8 and 2009-14, so we need to
    # get them in separate dataframes

    # Get the multi-year ameriflux dataframe
    site_df = ld.get_multiyr_aflx( site, datapath, gapfilled=True, 
                                   startyear=2007, endyear=endyear )
    #ipdb.set_trace()

    
    site_df = site_df[['TA_F', 'RH_F', 'PA', 'WS', 'WD', 'SW_IN_F', 
            'SW_OUT', 'LW_IN', 'LW_OUT']]

    # Export
    site_df.to_csv( '../processed_data/' + site + '_met_UW_Ecoclimate.csv',
            na_rep = '-9999')


# Function for plotting fixed and original data
#def plotfixed(df, var1):
#    # Plot filled series over original data
#    plt.figure()
#    plt.plot(df.index, df[var1], '-r', df.index, df[var1 + '_fixed'], '-b')
#    #plt.plot(df.index, df[var2], 'om')
#    plt.legend(['Orig ' + var1, 'Fixed ' + var1, 'Lin'])
#    plt.title(var1 + ' data filling')
