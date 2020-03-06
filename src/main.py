import time
import sys
from Report import Report


rpt = Report()


if len(sys.argv) < 2:
    print("Usage: src/main.py DATA_DIRECTORY")
    exit()

print("Reading the databases...", file=sys.stderr)
before = time.time()

fips_num = ''
location = ''

filename = f"{sys.argv[1]}/area_titles.csv"
f = open(filename)
# Convert the file 'sys.argv[1]/area_titles.csv' into a dictionary")
data_set = {}

for line in f:
    values = line.split(',', 1)
    if values[1] in data_set:
        if line[3:6] != '000' and line[1:3] != 'US' and line[1] != 'C' and line[1] != 'M':
            data_set.update({values[0]: values[1]})
    else:
        data_set.update({values[0] : values[1]})

f.close()

# for key in data_set:
#     print(f"{data_set[key]} {key}")


filename2 = f"{sys.argv[1]}/2018.annual.singlefile.csv"
f = open(filename2)
# Collect information from 'sys.argv[1]/2018.annual.singlefile.csv', place into the Report object rpt")

all_num_fips_areas = 0

all_gross_annual_wages = 0
all_area_max_annual_wage = ''
all_max_rep_wage = 0

all_total_num_establishments = 0
all_area_most_establishments = 0
all_max_num_establishments = 0

all_gross_annual_employment_lvl = 0
all_area_max_employment = 0
all_max_rep_employment_lvl = 0


all_data_dict = {}
for line in f:
    all_data = line.split(',')
    if all_data[1] in all_data_dict:
        if line[3:6] != '000' and line[1:3] != 'US' and line[1] != 'C' and line[1] != 'M':
            if all_data[1] == '"0"' and all_data[2] == '"10"':
                all_num_fips_areas += 1
                all_data_dict[all_data[1]].append(all_data[0])
                all_gross_annual_wages += int(all_data[10])
                all_total_num_establishments += int(all_data[8])
                all_gross_annual_employment_lvl += int(all_data[9])

                if all_max_rep_wage < int(all_data[10]):
                    all_max_rep_wage = int(all_data[10])
                    all_area_max_annual_wage = data_set.get(all_data[0])

                if all_max_num_establishments < int(all_data[8]):
                    all_max_num_establishments = int(all_data[8])
                    all_area_most_establishments = data_set.get(all_data[0])

                if all_max_rep_employment_lvl < int(all_data[9]):
                    all_max_rep_employment_lvl = int(all_data[9])
                    all_area_max_employment = data_set.get(all_data[0])

    else:
        all_data_dict[all_data[1]] = [all_data[0]]


f.close()

f = open(filename2)

soft_num_fips_areas = 0

soft_gross_annual_wages = 0
soft_area_max_annual_wage = ''
soft_max_rep_wage = 0

soft_total_num_establishments = 0
soft_area_most_establishments = ''
soft_max_num_establishments = 0

soft_gross_annual_employment_lvl = 0
soft_area_max_employment = ''
soft_max_rep_employment_lvl = 0



soft_data_dict = {}
for line in f:
    soft_data = line.split(',')
    if soft_data[1] in soft_data_dict:
        if line[3:6] != '000' and line[1:3] != 'US' and line[1] != 'C' and line[1] != 'M':
            if soft_data[1] == '"5"' and soft_data[2] == '"5112"':
                soft_num_fips_areas += 1
                soft_data_dict[soft_data[1]].append(soft_data[0])
                soft_gross_annual_wages += int(soft_data[10])
                soft_total_num_establishments += int(soft_data[8])
                soft_gross_annual_employment_lvl += int(soft_data[9])



                if soft_max_rep_wage < int(soft_data[10]):
                    soft_max_rep_wage = int(soft_data[10])
                    soft_area_max_annual_wage = data_set.get(soft_data[0])

                if soft_max_num_establishments < int(soft_data[8]):
                    soft_max_num_establishments = int(soft_data[8])
                    soft_area_most_establishments = data_set.get(soft_data[0])

                if soft_max_rep_employment_lvl < int(soft_data[9]):
                    soft_max_rep_employment_lvl = int(soft_data[9])
                    soft_area_max_employment = data_set.get(soft_data[0])


    else:
        soft_data_dict[soft_data[1]] = [soft_data[0]]

f.close()

after = time.time()
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)



# Fill in the report for all industries")
rpt.all.num_areas           = all_num_fips_areas

rpt.all.gross_annual_wages  = all_gross_annual_wages
rpt.all.max_annual_wage     = (all_area_max_annual_wage.strip().replace('"', ''), all_max_rep_wage)

rpt.all.total_estab         = all_total_num_establishments
rpt.all.max_estab           = (all_area_most_establishments.strip().replace('"', ''), all_max_num_establishments)

rpt.all.total_empl          = all_gross_annual_employment_lvl
rpt.all.max_empl            = (all_area_max_employment.strip().replace('"', ''), all_max_rep_employment_lvl)


# Fill in the report for the software publishing industry")
rpt.soft.num_areas          = soft_num_fips_areas

rpt.soft.gross_annual_wages = soft_gross_annual_wages
rpt.soft.max_annual_wage    = (soft_area_max_annual_wage.strip().replace('"', ''), soft_max_rep_wage)

rpt.soft.total_estab        = soft_total_num_establishments
rpt.soft.max_estab          = (soft_area_most_establishments.strip().replace('"', ''), soft_max_num_establishments)

rpt.soft.total_empl         = soft_gross_annual_employment_lvl
rpt.soft.max_empl           = (soft_area_max_employment.strip().replace('"', ''), soft_max_rep_employment_lvl)


# Print the completed report
print(rpt)

