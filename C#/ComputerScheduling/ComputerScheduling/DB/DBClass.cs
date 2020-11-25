using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.DataSqlClient;

namespace ComputerScheduling.DB
{
    public static class DBClass
    {      
        private static SqlConnection con = null; // static => 객체를 생성해서 사용하는 것이 아니라 클래스에 직접 접근하여 사용..?하는건가..
        private static bool SqlConState = false; 
        //public static DBClass(){} //초기화
        public static String server{get;set;}
        public static String dbName{get;set;}
        public static String userId{get;set;}
        public static String passWord{get;set;}
        
        #region DBConnect
        public static void DBConnect()
        {
            try
            {
                if(!SqlConState) 
                {
                    con = new SqlConnection($"Data Source={server}; Initial Catalog={dbName}; User ID={userId}; Password={passWord}");                    
                }  
		con.Open();                                
                SqlConState = true;
            }
            catch(Exception e)
            {
                MessageBox.Show(e.ToString());
            }
            
        }   
        #endregion
        
        #region DBDisConnect
        public static void DBDisConnect()
        {
            try
            {
                if(SqlConState) 
                {                    
                    con.Close();
                }
                
                SqlConState = false;                
            }
            catch(Exception e)
            {
                MessageBox.Show(e.ToString());
            }
        }
        #endregion
        
        #region INSERT
	//DBClass.SqlInsert(TBname, DBClass.InsertCols("one", "two", "three"), DBClass.InsertValues(5, NULL, "KIST"));
        public static void SqlInsert(String tbName, String col, String val)		
        {
	    SqlTransaction transaction;
            try
            {
                if(!SqlConState) 
                {
                    DBConnect();
                }
		transaction    = con.BeginTransaction("insert");
		    
                String insert_A = "INSERT INTO " + tbName + "(";
                insert_A += col;
                insert_A += ") ";
                insert_A += "VALUES(";
                insert_A +- val;
                insert_A += ")";
		    
		SqlCommand cmdInsert = new SqlCommand(insert_A, con);
		    cmdInsert.Transaction = transaction;
		cmdInsert.ExecuteNonQuery();	
		    transaction.Commit();
            }
            catch(Exception e)
            {
                MessageBox.Show(e.ToString());
		    transaction.Rollback();
            }
        
        }        
        #endregion        
	//value col 부분은 나중에 이런 함수가 많아지면 새로운 클래스로 옮기기(Static으로..)
        #region INSERT VALUE 
        public static String InsertValues(Params Object[] vals)
        {
            String allVals = "";
            
            for(int valLen = 0; valLen < vals.Length(); valLen++)
            {
	    	if(vals[valLen].GetType() == typeof(int))
		{
			allVals += vals[valLen].ToString();
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
        
        #region INSERT, SELECT COL 
        public static String InsertCols(Params String[] cols)
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
		
	#region SELECT        
        public static void SqlSelect(String tbName, String col, String where = "") //DBClass.SqlInsert(TBname, DBClass.InsertCols("one", "two", "three"), DBClass.InsertValues(5, NULL, "KIST"));
        {
	    SqlDataReader sqlRead = null;

            try
            {
                if(!SqlConState) 
                {
                    DBConnect();
                }
                String select_A = "SELECT " + col;
		select_A += " FROM " + tbName;
		//select_A += " WHERE 1=1 ";
		//select_A += " AND "  
		
		SqlCommand cmdSelect = new SqlCommand(select_A, con);
		sqlRead = cmdSelect.ExecuteReader();
		    
		while(sqlRead.Read())
		{
		    ReadSingleRow((IDataRecord)sqlRead);
		}
            }
            catch(Exception e)
            {
                MessageBox.Show(e.ToString());
            }
	    finally
	    {
		    sqlRead.Close();
	    }
        }     
    
	    private static void ReadSingleRow(IDataRecord sqlRead)
	    {
		    String rd = "";
		    int sqli = 0;
		    foreach(var sr in sqlRead)
		    {
			    sqli++;
			   rd += sr.ToString(); 
			   if(sqlRead.Length()-1 == sqli)break;   
			   rd +=  "\t";
		    }
		    Console.WriteLine(rd);
		    
		//Console.WriteLine(String.Format("{0}, {1}", sqlRead[0], sqlRead[1]));
	    }    	    
        #endregion 
		
	#region DELETE 
         public static void SqlDelete(String tbName, String where = "") 		
        {
	    SqlTransaction transaction;
            try
            {
                if(!SqlConState) 
                {
                    DBConnect();
                }
		transaction    = con.BeginTransaction("delete");
		    
                String delete_A = "DELETE FROM " + tbName;
                //delete_A += " WHERE";
               // delete_A += ;
		    
		SqlCommand cmdDelete = new SqlCommand(delete_A, con);
		    cmdDelete.Transaction = transaction;
		cmdDelete.ExecuteNonQuery();	
		    transaction.Commit();
            }
            catch(Exception e)
            {
                MessageBox.Show(e.ToString());
		    transaction.Rollback();
            }
        
        }     
        #endregion
        
		
        
    }
}
