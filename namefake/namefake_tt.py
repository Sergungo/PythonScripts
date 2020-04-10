import json
import requests
import workerpool

allcontents = []


class DownloadJob(workerpool.Job):

    # "Job for downloading a given URL."
    def __init__(self, url):
        self.url = url

    # The url we'll need to download when the job runs
    def run(self):
        try:
            data = requests.get(self.url)
            # print(data.text)
            allcontents.append(data.text)
            data.close()
        except requests.exceptions.ConnectionError:
            "Connection refused"


# create list of set amount of urls
def createUrlList(number):
    urls = []
    url = 'https://api.namefake.com/english-united-kingdom/random'
    while len(urls) < number:
        urls.append(url)
    return urls


# Breaks each name to two words
def getNames(allcontents):
    allnames = []

    try:
        i = 0
        while i < 100:
            response = json.loads(allcontents[i])
            # print(str(response["name"]).split(' '))
            names = str(response["name"]).split(' ')
            allnames = allnames + names
            i += 1
    except IndexError:
        "Index error"

    return allnames


# count each name among all names
def countSameNames(allnames):
    counted = []
    usedNames = []

    for name in allnames:
        if (usedNames.count(name) == 0):
            usedNames.append(name)
            count = allnames.count(name)
            counted.append((name, str(count)))

    return counted


def sortAndOutput(counted):
    counted.sort(key=lambda item: item[1], reverse=True)

    output_res = []

    for item in counted:
        if counted.index(item) < 5:
            output_res.append(item[0] + " " + item[1])
            print(item[0] + " " + item[1])

    return output_res


def main():
    urls = createUrlList(105)

    pool = workerpool.WorkerPool(size=50)

    for url in urls:
        job = DownloadJob(url.strip())
        pool.put(job)

    pool.shutdown()
    pool.wait()

    allnames = getNames(allcontents)

    counted = countSameNames(allnames)

    result = sortAndOutput(counted)
    # print(result)


if __name__ == '__main__':
    main()

