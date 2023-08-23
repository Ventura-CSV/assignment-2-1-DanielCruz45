def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    
    #asks for input of genders in class, messages added for clarity for in reguards to the gender your giving a number to
    male = int(input ('male count '))
    female= int(input('female count '))

    #finds the class total through adding the genders input
    total= male + female

    #calc the % of each gender reported
    m_perc= (male / total) * 100
    f_perc= (female / total) * 100

    #displays all values under the desired format and out puts them
    print(f'The total number of students: \t \t {total}')
    print(f'The number of males and females: \t {male} \t {female}')
    print(f'The percentage of males and females: \t{m_perc:.2f}% \t{f_perc:.2f}%')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
