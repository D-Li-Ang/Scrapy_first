from day04.myjobspider.myjobspider.dao.jobdao import JobDao

jobdao=JobDao()

resultSet=jobdao.selectAvgSalaryByjobType()
print('======================================')
print(resultSet)
resultSet=jobdao.selectAvgSalaryByjobCity()
print('======================================')
print(resultSet)
resultSet=jobdao.selectAvgSalaryByjobCity_jobType()
print('======================================')
print(resultSet)
resultSet=jobdao.selectJobNumberByjobCity_jobType()
print('======================================')
print(resultSet)
