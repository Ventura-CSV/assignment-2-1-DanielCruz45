def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    male = int(input ('male head count'))
    female= int(input('female head count'))

    total= male + female

    m_perc= 0
    f_perc= 0

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
