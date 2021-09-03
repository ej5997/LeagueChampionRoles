# LeagueChampionRoles
Uses na.op.gg to generate lists that represent champions played in each role.

Each list contains champions that are commonly played in that respective role, according to op.gg.

This should make data collection easier for some people and will greatly assist me in the development of my app located here: <p align="center">![GitHub release (latest by date)](https://img.shields.io/github/v/release/ej5997/RandomChampAndroidApp?style=plastic)</p>
This script relies on the usage of the BeautifulSoup and requests libraries. Additionally, it is dependent upon op.gg's site layout (HTML). It is incredibly sensitive to site changes and may fall apart if the website is altered in the future.

## Sample output (as of 9/3/21):

> Top:
> 
> ['Aatrox', 'Akali', 'Akshan', 'Camille', 'Cassiopeia', "Cho'Gath", 'Darius', 'Dr. Mundo', 'Fiora', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Gwen', 'Heimerdinger', 'Illaoi', 'Irelia', 'Jax', 'Jayce', 'Kayle', 'Kennen', 'Kled', 'Lillia', 'Lucian', 'Malphite', 'Maokai', 'Mordekaiser', 'Nasus', 'Ornn', 'Pantheon', 'Poppy', 'Quinn', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Sett', 'Shen', 'Singed', 'Sion', 'Sylas', 'Tahm Kench', 'Teemo', 'Trundle', 'Tryndamere', 'Urgot', 'Vayne', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Yasuo', 'Yone', 'Yorick', 'Zac']
> 
> 
> 
> Jgl:
> 
> ['Amumu', 'Diana', 'Ekko', 'Elise', 'Evelynn', 'Fiddlesticks', 'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Ivern', 'Jarvan IV', 'Jax', 'Karthus', 'Kayn', "Kha'Zix", 'Kindred', 'Lee Sin', 'Lillia', 'Master Yi', 'Nidalee', 'Nocturne', 'Nunu & Willump', 'Olaf', 'Poppy', 'Rammus', "Rek'Sai", 'Rengar', 'Rumble', 'Sejuani', 'Shaco', 'Shyvana', 'Taliyah', 'Trundle', 'Udyr', 'Vi', 'Viego', 'Volibear', 'Warwick', 'Xin Zhao', 'Zac']
> 
> 
> 
> Mid:
> 
> ['Aatrox', 'Ahri', 'Akali', 'Akshan', 'Anivia', 'Annie', 'Aurelion Sol', 'Azir', 'Cassiopeia', 'Corki', 'Diana', 'Ekko', 'Fizz', 'Galio', 'Garen', 'Graves', 'Heimerdinger', 'Irelia', 'Jayce', 'Kassadin', 'Katarina', 'Kennen', 'LeBlanc', 'Lissandra', 'Lucian', 'Lux', 'Malphite', 'Malzahar', 'Neeko', 'Nunu & Willump', 'Orianna', 'Pantheon', 'Qiyana', 'Renekton', 'Riven', 'Rumble', 'Ryze', 'Sett', 'Sylas', 'Syndra', 'Talon', 'Tryndamere', 'Twisted Fate', 'Veigar', 'Viego', 'Viktor', 'Vladimir', 'Xerath', 'Yasuo', 'Yone', 'Zed', 'Ziggs', 'Zoe']
> 
> 
> 
> ADC:
> 
> ['Aphelios', 'Ashe', 'Caitlyn', 'Cassiopeia', 'Draven', 'Ezreal', 'Jhin', 'Jinx', "Kai'Sa", 'Kalista', "Kog'Maw", 'Lucian', 'Miss Fortune', 'Samira', 'Senna', 'Sivir', 'Swain', 'Syndra', 'Tristana', 'Twitch', 'Varus', 'Vayne', 'Xayah', 'Yasuo', 'Ziggs']
> 
> 
> 
> Supp:
> 
> ['Alistar', 'Amumu', 'Anivia', 'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Galio', 'Gragas', 'Janna', 'Karma', 'Leona', 'Lulu', 'Lux', 'Maokai', 'Morgana', 'Nami', 'Nautilus', 'Pantheon', 'Poppy', 'Pyke', 'Rakan', 'Rell', 'Senna', 'Seraphine', 'Sett', 'Shaco', 'Shen', 'Sona', 'Soraka', 'Swain', 'Tahm Kench', 'Taric', 'Thresh', 'Trundle', 'Veigar', "Vel'Koz", 'Xerath', 'Yuumi', 'Zac', 'Zilean', 'Zyra']

