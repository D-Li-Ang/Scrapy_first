from ..dao.basedao import BaseDao
import time

class JobDao(BaseDao):
    def createJobInfo(self, params=[]):
        sql = "insert into t_job (jobType,jobName,jobCompany,jobAdress,jobSalary,jobDate,jobURL,jobContext,jobCity,jobMinSalary,jobMaxSalary,jobMeanSalary) " \
              "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        result = self.execute(sql, params)
        self.commit()
        return result
    def selectAvgSalaryByjobType(self):
        sql= "select jobType,avg(jobMeanSalary) as salary from t_job group by jobType"
        result = self.execute(sql)
        resultSet = self.fetch()
        self.commit()
        return resultSet
    def selectAvgSalaryByjobCity(self):
        sql = "select jobCity,avg(jobMeanSalary) as salary from t_job group by jobCity"
        result = self.execute(sql)
        resultSet = self.fetch()
        self.commit()
        return resultSet
    def selectAvgSalaryByjobCity_jobType(self):
        sql = "select jobCity,jobType,avg(jobMeanSalary) as salary from t_job group by jobCity ,jobType"
        result = self.execute(sql)
        resultSet = self.fetch()
        self.commit()
        return resultSet

    def selectJobNumberByjobCity_jobType(self):
        sql = "select jobCity,jobType,count(*) as jobcount from t_job group by jobCity ,jobType"
        result = self.execute(sql)
        resultSet = self.fetch()
        self.commit()
        return resultSet
