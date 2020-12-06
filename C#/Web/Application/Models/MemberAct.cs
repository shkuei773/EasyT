using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Application.Data;

namespace Application.Models
{
    public class MemberAct
    {
        public List<Member> GetMember(int paramMemberNumber)
        {
            MemberData memberData = new MemberData();
            return memberData.members; //LINQ
        }
    }
}