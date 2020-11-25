using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.DataSqlClient;

#define IFNOTCON if(!SqlConState)     
#define IFCON if(SqlConState) 

namespace ComputerScheduling.DB
{
    public class DBClass
    {      
        private static SqlConnection con = null; // static => 객체를 생성해서 사용하는 것이 아니라 클래스에 직접 접근하여 사용..?하는건가..
        private static bool SqlConState = false; 
        public DBClass(){}
        public String server{get;set;}
        public String dbName{get;set;}
        public String userId{get;set;}
        public String passWord{get;set;}
        
        #region DBConnect
        public static void DBConnect()
        {
            try
            {
                IFNOTCON
                {
                    con = new SqlConnection($"Data Source={server}; Initial Catalog={dbName}; User ID={userId}; Password={passWord}");
                    con.Open();
                }  
                                
                SqlConState = true;
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
        public static void DBDisConnect()
        {
            try
            {
                IFCON
                {                    
                    con.Close();
                }
                
                SqlConState = false;                
            }
            catch(Exception e)
            {
            }
            finally
            {
            }
        }
        #endregion
        
        #region INSERT
        public void SqlInsert(String tbName, String col1, String col2, String val1, String val2)
        {
            try
            {
                IFNOTCON
                {
                    DBConnect();
                }
                String insert_A = "INSERT INTO " + tbName + "(";
                insert_A += col1 +", ";
                insert_A += col2 +") ";
                insert_A += "VALUES(";
                insert_A +- "'" + val1 + "', ";
                insert_A += "'" + val2 + "'";
                insert_A += ")";                
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
