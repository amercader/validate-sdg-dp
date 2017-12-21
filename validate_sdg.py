from datapackage import Package
from goodtables import validate


def main():

    base_url = 'https://raw.githubusercontent.com/UNStats/SDG/master/DataPackages/Goal/{}/datapackage.json'

    for goal in range(1, 18):
        dp_url = base_url.format(goal)
        dp = Package(dp_url)

        print('# Validating SDG {}'.format(goal))
        if dp.valid:
            print('\tData Package descriptor valid')
        else:
            print('\tData Package descriptor invalid')
            print('\t\tErrors:')
            print('\n'.join(['\t\t\t' + str(error) for error in dp.errors]))

        report = validate(dp_url, row_limit=10000)
        if report['valid']:
            print('\tData valid')
        else:
            print('\tData invalid')
            print('\t\tErrors (first 20):')
            for table in report['tables']:
                if not table['valid']:
                    print('\t\t\t{}:'.format(table['source'].split('/')[-1]))
                    cnt = 0
                    for error in table['errors']:
                        cnt += 1
                        print('\t\t\t\t\t' + error['message'])
                        if cnt > 20:
                            break

if __name__ == '__main__':
    main()
