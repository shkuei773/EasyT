using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using Application.Models;

namespace Application.Controllers
{
    public class BoardController : Controller
    {
        public ActionResult List()
        {
            //if (Id == null) return HttpNotFound("Error Message");//content => 텍스트 보여주기

            DocumentAct documentAct = new DocumentAct();
            MemberAct memberAct = new MemberAct();

            var members = memberAct.GetMember(1);
            var documents = documentAct.GetDocuments();

            //ViewBag.Member = members;
            ViewData["Member"] = members;

            return View(documents);
        }
    }
}