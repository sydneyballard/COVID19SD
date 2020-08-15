import pandas as pd
# import vincent as vn
import matplotlib as mpl
import matplotlib.pyplot as plt

# Load and read data
zipcode_csv = pd.read_csv(r"data",
                          names=['zip', 'city', 'cases', 'case_rate', 'case_rate_ratio', 'income', 'income_ratio'])
zipcode_df = pd.DataFrame(zipcode_csv)

# Helps column view when printing output (doesn't truncate as much!)
pd.set_option('display.expand_frame_repr', False)


# Visualize stack plots: zip v. COVID-19 , income v. COVID-19
def stack_plot(x, y):
    # Set title
    plt.title('COVID-19 case reports in relation '
              'to household income')

    # Set independent and dependent vars
    labels = ["Household income",
              "COVID-19 Rate"]

    # Common var
    y = [float(num) for num in y]
    plt.xlabel('Zip code')
    plt.ylabel('Relative ratio')

    # # Set colors
    # colors = ['springgreen',
    #           'lightslategray']

    plt.stackplot(x, y,
                  labels=labels,
                  edgecolor='black')
    matplotlib.axes
    # Plots to upper left
    plt.legend(loc=2)
    plt.show()


# Visualizer map


if __name__ == '__main__':
    # print(zipcode_csv)
    print(zipcode_df)

    # Set plt style
    plt.style.use('classic')

    # Sort values by ascending income (makes visualization better)
    # zipcode_df.income = zipcode_df.income.asType(float)
    sorted_by_income_df = zipcode_df.dropna().sort_values('income')
    print("\n SORTED: \n\n {x}".format(x=sorted_by_income_df))

    # Manipulate data frame
    zip = sorted_by_income_df.loc[:, 'zip']
    income_ratio = sorted_by_income_df.loc[:, 'income_ratio']
    covid_rate_ratio = sorted_by_income_df.loc[:, 'case_rate_ratio']

    # DEBUG PRINTING ; DF IS CORRECT
    print("\nZIP CODES: \n\n{x}".format(x=zip))
    print("\nMEDIAN INCOME (RATIO): \n\n{x}".format(x=income_ratio))
    print(stack_plot(income_ratio, covid_rate_ratio))
