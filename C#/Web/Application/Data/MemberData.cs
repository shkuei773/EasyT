using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Application.Models;

namespace Application.Data
{
    public class MemberData
    {
        public List<Member> members
        {
            get 
            {
                return new List<Member>
                {
                    new Member{ Member_Number = 1, Id = "Lee", Name = "이순신", Password = "1234"},
                    new Member{ Member_Number = 2, Id = "Jung", Name = "오순신", Password = "123"},
                    new Member{ Member_Number = 3, Id = "ban", Name = "김순신", Password = "12"},
                    new Member{ Member_Number = 4, Id = "su", Name = "나순신", Password = "1"}
                };
            }
        }
    }
}