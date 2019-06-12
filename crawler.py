from bs4 import BeautifulSoup
import csv
  
def parse(html):#собираем данные со страницы
    soup = BeautifulSoup(html)
  
    teams = []
    
    for row in soup.select('tbody > tr'):
            cols = row.select('td')
    
            teams.append({
                'Место': cols[0].text,
                'Команда': [name.text for name in row.select('a[class=name]')],
                'Матчи': cols[2].text
            })
  
    return teams
  
def save(teams,path):   #ФУНКЦИЯ ЗАПИСИ СПАРСЕННЫХ ФАЙЛОВ В CSV ФАЙЛ
    with open(path,'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Место','Команда','Матчи'))
  
        for team in teams:
            writer.writerow((team['Место'],team['Команда'],team['Матчи']))
  
  
if __name__ == '__main__':
    url = 'https://www.sports.ru/epl/table/'
  
    import urllib.request
    with urllib.request.urlopen(url) as rs:
        html = rs.read()
  
    teams = parse(html)
  
    save(teams,'апл.csv')
  
    for team in teams:
        print(team)