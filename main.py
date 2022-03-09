from data.db_session import global_init, create_session
from data.jobs import Jobs
from data.user import User

global_init("database.db")
session = create_session()
user1 = User()
user1.surname = "Scott"
user1.name = "Ridley"
user1.age = 21
user1.position = "captain"
user1.speciality = "research engineer"
user1.address = "module_1"
user1.email = "scott_chief@mars.org"
user1.set_password("cap")
# pbkdf2:sha256:260000$ujbbSa9xhRSAcVDd$5303b8dd3e53a9f4b8bb643949eeb66a78dcb96e134f1b6299f5abf243d466c7
# pbkdf2:sha256:260000$3NOgwGz6rTm7fwJC$4a0dfc30b913192e3bed522be90c96baa87f5fc3b59f8e64625ed09873b63c42
user2 = User()
user2.surname = "Герасимов"
user2.name = "Роман"
user2.age = 24
user2.position = "teacher"
user2.speciality = "junior researcher"
user2.address = "module_1"
user2.email = "romagrizly@gmail.com"
user2.set_password("blabla")

user3 = User()
user3.surname = "Мельников"
user3.name = "Степан"
user3.age = 15
user3.position = "student"
user3.speciality = "junior python developer"
user3.address = "module_python"
user3.email = "stepan_melnikoff@gmail.com"
user3.set_password("password")

session.add(user1)
session.add(user2)
session.add(user3)

job = Jobs()
job.team_leader = 1
job.job = 'deployment of residential modules 1 and 2'
job.work_size = 15
job.collaborators = '2, 3'
job.is_finished = False
session.add(job)
session.commit()
session.close()
