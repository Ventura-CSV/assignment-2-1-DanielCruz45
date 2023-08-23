def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    
    #asks for input of genders in class
    male = int(input ('male head count'))
    female= int(input('female head count'))

    #finds the class total through adding the genders input
    total= male + female

    #calc the % of each gender reported
    m_perc= (male / total) * 100
    f_perc= (female / total) * 100

    #displays all values under the desired format and out puts them
    print(total)
    print({male}, {female})
    print({m_perc}, {f_perc})

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
