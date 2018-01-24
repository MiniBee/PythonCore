
def safe_float(obj):
    try:
        return float(obj)
    except (ValueError, TypeError) as e:
        return e


def main():
    'handles all the data processing'
    log = open('/home/phy/data/cardlog.txt', 'w')
    try:
        ccfile = open('/homw/phy/data/carddata.txt', 'r')
    except IOError as e:
        log.write('no txns this month\n')
        log.close()
        return
    txns = ccfile.readlines()
    ccfile.close()
    total = 0.0
    log.write('account log: \n')

    for eachTxn in txns:
        result = safe_float(eachTxn)
        if isinstance(result, float):
            total += result
            log.write('data...processed\n')
        else:
            log.write('ignored: %s' % result)
    print('$%.2f (new balance)' % total)
    log.close()



if __name__ == '__main__':
    main()