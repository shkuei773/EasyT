using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.DataSqlClient;

namespace ComputerScheduling.DB
{
    class DBClass
    {      
        private SqlConnection con = null;
        public DBClass(){};
        public String server{get;set;}
        public String dbName{get;set;}
        public String userId{get;set;}
        public String passWord{get;set;}
        
        public DBConnection()
        {
            con = new SqlConnection($"Data Source={server}; Initial Catalog={dbName}; User ID={userId}; Password={passWord});
        }        
    }
}
