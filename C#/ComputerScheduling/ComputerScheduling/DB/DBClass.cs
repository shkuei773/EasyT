﻿using System;
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
        /*
        	object[] myObjArray = { 2, 'b', "test", "again" };		
		    Console.WriteLine(myObjArray[0].GetType() == typeof(int));
        */
        public void SqlInsert(String tbName, String col, String val) //DBClass.SqlInsert(TBname, DBClass.InsertCols("one", "two", "three"), DBClass.InsertValues(5, NULL, "KIST"));
        {
            try
            {
                IFNOTCON
                {
                    DBConnect();
                }
                String insert_A = "INSERT INTO " + tbName + "(";
                insert_A += col;
                insert_A += ") ";
                insert_A += "VALUES(";
                insert_A +- val1;
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
        
	//value col 부분은 새로운 클래스에 옮겨도 될듯(
        #region INSERT VALUE 
        public String InsertValues(Params Object[] vals)
        {
            String allVals = "";
            
            for(int valLen = 0; valLen < vals.Length(); valLen++)
            {
	    	if(vals[valLen].GetType() == typeof(int))
		{
			allVals += vals[valLen].toString;
			if(vals.Length() - 1 <= valLen) break;
			allVals += ", ";    
		}
		else
		{
			allVals += "'"; 
			allVals += vals[valLen] == "NULL"? "":vals[valLen] ;
			if(vals.Length() - 1 <= valLen) break;
			allVals += "', ";    
		}             
            }            
            return allVals;
        }        
        #endregion
        
        
        #region INSERT COL 
        public String InsertCols(Params String[] cols)
        {
            String allCols = "";
            
            for(int colLen = 0; colLen < cols.Length(); colLen++)
            { 
                allCols += cols[colLen];
                if(cols.Length() - 1 <= colLen) break;
                allCols += ", ";                
            }            
            return allCols;
        }        
        #endregion
        
        
    }
}
