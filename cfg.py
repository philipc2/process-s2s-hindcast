

# Paths
base_path = "/glade/scratch/philipc/s2s-reforecast-data/"
input_path = base_path + "orig_data/"
output_path = base_path + "data/"

# {var} {month 'xx'} {year 'xxxx}
vym_str = "{}/{}/{}/"

# {var} {start_date 'xx'} {month 'xx'} {year 'xx'} {member 'xx}
cv_str = "{}_cesm2cam6v2_{}{}{}_00z_d01_d46_m{}.nc"

# S2S Hindcase Covariate Information
members = [f'0{m}' if m < 10 else f'{m}' for m in range(1, 11)]
covariates = ['ts', 'tas_2m', 'zg_10', 'zg_500', 'psl']

years = [year for year in range(2000, 2023)]
months_n = [f'0{m}' if m < 10 else f'{m}' for m in range(1, 13)]
months_str = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
