using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.DataSqlClient;

define 

namespace ComputerScheduling.DB
{
    public class DBClass
    {      
        private static SqlConnection con = null; // static => 객체를 생성해서 사용하는 것이 아니라 클래스를 직접사용..?하는건가..
        private static bool SqlConState = false; 
        public DBClass(){}
        public String server{get;set;}
        public String dbName{get;set;}
        public String userId{get;set;}
        public String passWord{get;set;}
        
        #region DBConnec
        public static DBConnect()
        {
            try
            {
                if(!SqlConState)
                {
                    con = new SqlConnection($"Data Source={server}; Initial Catalog={dbName}; User ID={userId}; Password={passWord}");
                }                                 
                
            }
            catch(Exception e)
            {
                
            }
            finally
            {
            
            }
            
        }   
        #endregion
        
        #region DBDisConnect
        public static DBDisConnect()
        {
            try
            {
            }
            catch(Exception e)
            {
            }
            finally
            {
            }
        }
        #endregion
        
    }
}
