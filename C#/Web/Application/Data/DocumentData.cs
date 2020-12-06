using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Application.Data
{
    public class DocumentData
    {
        public List<Models.Document> Documents
        {
            get
            {
                List<Models.Document> returnValue = new List<Models.Document>
                {
                    new Models.Document{ Document_Number=1,Title = "공지사항입니다.", Writer="홍길동"},
                    new Models.Document { Document_Number = 2, Title = "제목입니다 #1.", Writer = "이순신" },
                    new Models.Document { Document_Number = 3, Title = "제목입니다 #2.", Writer = "신사입당" },
                    new Models.Document { Document_Number = 4, Title = "제목입니다 #3.", Writer = "너는뭐임" },
                    new Models.Document { Document_Number = 5, Title = "제목입니다 #4.", Writer = "너임" },
                    new Models.Document { Document_Number = 6, Title = "제목입니다 #5.", Writer = "너" }
                };
                return returnValue;
            }
        }
    }
}