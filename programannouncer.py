from flask import *
from Dbconnection import Db
app = Flask(__name__)
app.secret_key="qaaaaaaaa"
staticpath = "C:\\Users\\91730\\PycharmProjects\\programannouncer\\static\\"

@app.route('/')
def program_announcer():
     return render_template('launching_index.html')

@app.route('/login')
def login():
    return render_template('login_index.html')

@app.route('/login_post', methods=['post'])
def login_post():

    username = request.form['textfield']
    password = request.form['textfield2']
    db=Db()
    res=db.selectOne("SELECT * FROM login WHERE `username`='"+username+"' AND `password`='"+password+"'")
    if res is not None:
        session['lid'] = res['login_id']
        if res['type']=="admin":
            return  redirect("/admin_home")
        elif res['type']=="artist":
            return  redirect("/artistpanel_home")
        else:
            return '''<script>alert('User Not Found')</script>'''
    else:
        return '''<script>alert('Inavlid Data');window.location="/login"</script>'''

@app.route('/admin_home')
def admin_home():
    return render_template('admin/home.html')

@app.route('/view_and_aprv_artistpanel')
def view_and_aprv_artistpanel():
    b = Db()
    qry ="SELECT * FROM artist_panel where status='pending'"
    res = b.select(qry)
    return render_template('admin/view_and_aprv_artistpanel.html',data=res)

@app.route('/approve_artist_panel/<id>')
def approve_artist_panel(id):
    e = Db()
    qry = "UPDATE `artist_panel` SET `status`='artist' WHERE `login_id`='"+str(id)+"'"
    res = e.update(qry)
    qry1 = "UPDATE `login` SET `type`='artist' WHERE `login_id`='"+str(id)+"'"
    res1 = e.update(qry1)
    return '''<script>alert('Approved Succesfully');window.location='/view_and_aprv_artistpanel'</script>'''

@app.route('/approve_artist_panelnew/<id>')
def approve_artist_panelnew(id):
    g = Db()
    qry = "UPDATE `artist_panel` SET `status`='artist' WHERE `login_id`='" + str(id) + "'"
    res = g.update(qry)
    qry2 = "UPDATE `login` SET `type`='artist' WHERE `login_id`='" + str(id) + "'"
    res2 = g.update(qry2)
    return "<script>alert('Approved successfully');window.location='/view_and_aprv_artistpanel'</script>"

@app.route('/reject_artist_panel/<id>')
def reject_artist_panel(id):
    g = Db()
    qry = "UPDATE `artist_panel` SET `status`='rejected' WHERE `login_id`='" + str(id) + "'"
    res = g.update(qry)
    qry2 = "UPDATE `login` SET `type`='rejected' WHERE `login_id`='" + str(id) + "'"
    res2 = g.update(qry2)
    return '''<script>alert('Rejected Succesfully');window.location='/view_and_aprv_artistpanel'</script>'''

@app.route('/reject_artist_panelnew/<id>')
def reject_artist_panelnew(id):
    g = Db()
    qry = "UPDATE `artist_panel` SET `status`='rejected' WHERE `login_id`='" + str(id) + "'"
    res = g.update(qry)
    qry2 = "UPDATE `login` SET `type`='rejected' WHERE `login_id`='" + str(id) + "'"
    res2 = g.update(qry2)
    return "<script>alert('Rejected successfully');window.location='/approved_artistpanel'</script>"


@app.route('/view_and_aprv_artistpanel_post', methods=['post'])
def view_and_aprv_artistpanel_post():
    s= request.form['textfield']
    b = Db()
    qry = "SELECT * FROM artist_panel where status='pending' and name like '%"+s+"%'"
    res = b.select(qry)

    return render_template('admin/view_and_aprv_artistpanel.html', data=res)


@app.route('/rejected_artistpanel')
def rejected_artistpanel():
    d = Db()
    qry = "SELECT * FROM `artist_panel` WHERE `status`='rejected'"
    res = d.select(qry)

    return render_template('admin/rejected_artistpanel.html',data=res)

@app.route('/rejected_artistpanel_post', methods=['post'])
def rejected_artistpanel_post():
    q = request.form['textfield']
    d = Db()
    qry = "SELECT * FROM `artist_panel` WHERE `status`='rejected' and name like '%"+q+"%'"
    res = d.select(qry)

    return render_template('admin/rejected_artistpanel.html',data=res)



@app.route('/approved_artistpanel')
def approved_artistpanel():
    c = Db()
    qry = "SELECT * FROM `artist_panel` WHERE `status`='artist'"
    res = c.select(qry)

    return render_template('admin/approved_artistpanel.html',data=res)






@app.route('/approved_artistpanel_post', methods=['post'])
def approved_artistpanel_post():
    s = request.form['textfield']
    c = Db()
    qry = "SELECT * FROM `artist_panel` WHERE `status`='artist' and name like '%"+s+"%'"
    res = c.select(qry)

    return render_template('admin/approved_artistpanel.html', data=res)





@app.route('/view_users')
def view_users():
    a = Db()
    qry ="SELECT * FROM USER"
    res = a.select(qry)

    return render_template('admin/view_users.html',data=res)

@app.route('/search_user', methods=['post'])
def search_user():
    search = request.form['textfield']
    db = Db()
    qry = "SELECT * FROM `user` WHERE `name` LIKE '%"+search+"%'"
    res = db.select(qry)
    print(res)
    return render_template('admin/view_users.html',data=res)



@app.route('/view_popular_programs_of_artist_panel')
def view_popular_programms_of_artist_panel():
    db = Db()
    qry = "SELECT `highlights`.*,`artist_panel`.`name` AS apname,`artist_panel`.`email` AS apemail, `artist_panel`.`phone` AS apphone,`category`.`program_name` FROM `artist_panel` INNER JOIN `highlights` ON `highlights`.`artist_panel_lid`=`artist_panel`.`login_id` INNER JOIN `category` ON `category`.`program_id`=`highlights`.`program_id`"
    res = db.select(qry)
    return render_template('admin/view_popular_programs_of_artist_panel.html',data=res)


@app.route('/search_highlights', methods=['post'])
def search_highlights():
    search_name = request.form['textfield']
    db = Db()
    qry = "SELECT `highlights`.*,`artist_panel`.`name` AS apname,`artist_panel`.`email` AS apemail, `artist_panel`.`phone` AS apphone,`category`.`program_name` FROM `artist_panel` INNER JOIN `highlights` ON `highlights`.`artist_panel_lid`=`artist_panel`.`login_id` INNER JOIN `category` ON `category`.`program_id`=`highlights`.`program_id` where category.program_name like '%"+search_name+"%' "
    res = db.select(qry)
    print(res)
    return render_template('admin/view_popular_programs_of_artist_panel.html',data=res)


@app.route('/view_complaints_and_send_reply')
def view_complaints_and_send_reply():
    f = Db()
    qry ="SELECT `complaints`.*,`user`.* FROM `complaints` JOIN `user` ON `user`.`login_id`=`complaints`.`user_lid` "
    res = f.select(qry)
    return render_template('admin/view_complaints_and_send_reply.html',data=res)

@app.route('/search_Complaint', methods=['post'])
def search_Complaint():
    frm_date = request.form['textfield']
    to_date = request.form['textfield2']
    db = Db()
    qry ="SELECT `complaints`.*,`user`.* FROM `complaints` JOIN `user` ON `user`.`login_id`=`complaints`.`user_lid` WHERE `complaints`.`date` BETWEEN '"+frm_date+"' AND '"+to_date+"'"
    res = db.select(qry)
    return render_template('admin/view_complaints_and_send_reply.html',data=res)

@app.route('/send_Reply/<cid>')
def send_Reply(cid):
    session['cid']=cid
    return render_template('admin/send_Reply.html')



@app.route('/replypost',methods=['post'])
def replypost():
    db=Db()
    reply=request.form['textarea']
    qry="UPDATE `complaints` SET `reply`='"+str(reply)+"',`status`='replied' WHERE `complaints_id`='"+str(session['cid'])+"'"
    db.update(qry)
    return redirect('view_complaints_and_send_reply')




@app.route('/adm_paswrd')
def adm_paswrd():
    return render_template('admin/change_paswrd.html')

@app.route('/adm_pswrd_post', methods=['post'])
def adm_pswrd_post():
    op = request.form['p1']
    np = request.form['p2']
    cnp = request.form['p3']
    db = Db()
    qry = "SELECT * FROM `login` WHERE `password`='"+op+"'"
    res = db.selectOne(qry)
    if res is not None:
        if np==cnp:
            qry = "UPDATE `login` SET `password`='"+cnp+"' where login_id='"+str(session['lid'])+"' "
            res = db.update(qry)
            print(res)
            return redirect('/login')
        else:
            return '''<script>alert('Invalid');window.location='/adm_paswrd'</script>'''
    else:
        return '''<script>alert('Invalid');window.location='/adm_paswrd'</script>'''




















































#second_module

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register_post',methods=['post'])
def register_post():
    district = request.form['select']

    name = request.form['textfield']
    place = request.form['textfield9']
    post = request.form['textfield11']
    pincode = request.form['textfield3']
    email = request.form['textfield4']
    phone = request.form['textfield5']
    joined = request.form['textfield7']
    latitude = request.form['textfield8']
    longitude = request.form['textfield10']
    password = request.form['hiddenField']

    logo = request.files['fileField']
    logo.save(staticpath+"artist\\"+logo.filename)
    path ="/static/artist/"+logo.filename


    db=Db()

    qry2="INSERT INTO `login` (`username`,`password`,`type`) VALUES ('"+email+"','"+password+"','pending')"
    res =db.insert(qry2)
    qry1 = "INSERT INTO`artist_panel`(`login_id`,`name`,`email`,`phone`,`place`,`post`,`district`,`pincode`,`logo`,`latitude`,`longitude`,`status`,est_year) VALUES ('"+str(res)+"','"+name+"','"+email+"','"+phone+"','"+place+"','"+post+"','"+district+"','"+pincode+"','"+path+"','"+latitude+"','"+longitude+"','pending','"+joined+"')"
    res1 = db.insert(qry1)
    return  "<script>alert('Account created successfully');window.location='/login'</script>"



@app.route('/artistpanel_home')
def artistpanel_home():
    return render_template('artist_panel/artistpanel.home.html')

@app.route('/view_profile')
def view_profile():
    a = Db()
    qry = "SELECT * FROM `artist_panel` WHERE login_id='"+str(session['lid'])+"'"
    res = a.selectOne(qry)
    return render_template('artist_panel/view_profile.html',data=res)

@app.route('/edit_profile/<id>')
def edit_profile(id):
    a = Db()
    qry = "SELECT * FROM `artist_panel` WHERE login_id='"+str(id)+"'"
    res = a.selectOne(qry)
    return render_template('artist_panel/edit_profile.html', data=res)

@app.route('/edit_profile_post',methods=['post'])
def edit_profile_post():
    id = request.form['h1']
    district = request.form['select']

    name = request.form['textfield']
    place = request.form['textfield9']
    post = request.form['textfield11']
    pincode = request.form['textfield3']
    email = request.form['textfield4']
    phone = request.form['textfield5']
    joined = request.form['textfield7']
    latitude = request.form['textfield8']
    longitude = request.form['textfield10']
    if 'fileField' in request.files!="":
        logo = request.files['fileField']
        if logo.filename!="":
            logo.save(staticpath+"artist\\"+logo.filename)
            path ="/static/artist/"+logo.filename

            db=Db()
            qry1 = "UPDATE `artist_panel` SET `name`='"+name+"', `email`='"+email+"', `phone`='"+phone+"',`place`='"+place+"',`post`='"+post+"',`district`='"+district+"',`pincode`='"+pincode+"',`logo`='"+path+"',`latitude`='"+latitude+"',`longitude`='"+longitude+"',`est_year`='"+joined+"' where login_id='"+str(id)+"' "
            res1 = db.update(qry1)
            return view_profile()
        else:
            db = Db()
            qry1 = "UPDATE `artist_panel` SET `name`='" + name + "', `email`='" + email + "', `phone`='" + phone + "',`place`='" + place + "',`post`='" + post + "',`district`='" + district + "',`pincode`='" + pincode + "',`latitude`='" + latitude + "',`longitude`='" + longitude + "',`est_year`='" + joined + "' where login_id='"+str(id)+"'"
            res1 = db.update(qry1)
            return view_profile()
    else:
        db = Db()
        qry1 = "UPDATE `artist_panel` SET `name`='" + name + "', `email`='" + email + "', `phone`='" + phone + "',`place`='" + place + "',`post`='" + post + "',`district`='" + district + "',`pincode`='" + pincode + "',`latitude`='" + latitude + "',`longitude`='" + longitude + "',`est_year`='" + joined + "' where login_id='"+str(id)+"'"
        res1 = db.update(qry1)
        return view_profile()



@app.route('/add_category')
def add_category():
    return render_template('artist_panel/add_category.html')

@app.route('/add_category_post',methods=['post'])
def add_category_post():
    programme = request.form['textfield']
    description = request.form['textarea']

    budget = request.form['textfield2']

    photo = request.files['fileField']
    photo.save(staticpath + "category\\" + photo.filename)
    path = "/static/category/" + photo.filename

    db=Db()
    qry="INSERT INTO `category`(`artist_panel_lid`,`program_name`,`description`,`photo`,`budget`) VALUES ('"+str(session['lid'])+"','"+programme+"','"+description+"','"+path+"','"+budget+"')"
    res=db.insert(qry)
    return render_template('artist_panel/add_category.html')


@app.route('/view_category')
def view_category():
    d = Db()
    qry = "SELECT * FROM `category` WHERE `artist_panel_lid`='"+str(session['lid'])+"'"
    res = d.select(qry)
    print(res)
    return render_template('artist_panel/view_category.html',data=res)

@app.route('/view_category_post',methods=['post'])
def view_category_post():
    d = Db()
    search = request.form['textfield']
    qry = "SELECT * FROM `category` WHERE `program_name` like '%"+search+"%'"
    res = d.select(qry)
    print(res)
    return render_template('artist_panel/view_category.html',data=res)


@app.route('/edit_category/<id>')
def edit_category(id):
    d = Db()
    qry = "SELECT * FROM `category` WHERE `program_id`='"+str(id)+"'"
    res = d.selectOne(qry)
    return render_template('artist_panel/edit_category.html',data=res)

@app.route('/edit_category_post',methods=['post'])
def edit_category_post():
    id = request.form['h1']
    programme = request.form['textfield']
    description = request.form['textarea']

    budget = request.form['textfield2']
    db = Db()
    if 'fileField' in request.files != "":
        photo = request.files['fileField']
        if photo.filename != "":
            photo.save(staticpath + "category\\" + photo.filename)
            path = "/static/category/" + photo.filename
            qry = "UPDATE `category` SET `program_name`='"+programme+"', `photo`='"+path+"',`description`='"+description+"',`budget`='"+budget+"' WHERE `program_id`='"+str(id)+"'"
            res = db.update(qry)
            return view_category()
        else:
            qry = "UPDATE `category` SET `program_name`='" + programme + "',`description`='" + description + "',`budget`='" + budget + "' WHERE `program_id`='" +str(id)+"'"
            res = db.update(qry)
            return view_category()
    else:
        qry = "UPDATE `category` SET `program_name`='" + programme + "', `description`='" + description + "',`budget`='" + budget + "' WHERE `program_id`='"+str(id)+"'"
        res = db.update(qry)
        return view_category()



@app.route('/delete_category/<id>')
def delete_category(id):
    d = Db()
    qry  = "DELETE FROM `category` WHERE `program_id`='"+id+"'"
    rea = d.delete(qry)
    return "<script>alert('Deleted Succesfully');window.location='/view_category'</script>"


@app.route('/add_member')
def add_member():
    db = Db()
    qry = "SELECT * FROM `category` WHERE `artist_panel_lid`='"+str(session['lid'])+"'"
    res = db.select(qry)
    return render_template('artist_panel/add_member.html',data=res)


@app.route('/add_member_post',methods=['post'])
def add_member_post():
    prgm = request.form['pgm']
    name=request.form['textfield']
    email=request.form['textfield2']
    phone=request.form['textfield3']
    gender=request.form['r1']
    place=request.form['textfield5']
    post=request.form['textfield7']
    district=request.form['textfield8']
    pincode=request.form['textfield9']
    photo = request.files['fileField']
    photo.save(staticpath + "member\\" + photo.filename)
    path = "/static/member/" + photo.filename

    db=Db()

    qry1 = "INSERT INTO `login` (`username`,`password`,`type`) VALUES ('"+email+"','"+phone+"','pending')"
    res1 = db.insert(qry1)
    qry="INSERT INTO `member`(`artist_panel_lid`,`name`,`email`,`phone`,`place`,`gender`,`post`,`district`,`pincode`,`photo`, member_lid,program_id) VALUES('"+str(session['lid'])+"','"+name+"','"+email+"','"+phone+"','"+place+"','"+gender+"','"+post+"','"+district+"','"+pincode+"','"+str(path)+"','"+str(res1)+"','"+str(prgm)+"')"
    res = db.insert(qry)

    return render_template('artist_panel/add_member.html')

@app.route('/view_member')
def view_member():
    db=Db()
    # qry="SELECT * FROM `member` WHERE `artist_panel_lid`='"+str(session['lid'])+"'"
    qry = "SELECT `member`.*,`category`.`program_name` FROM `category` INNER JOIN `member` ON `member`.`program_id`=`category`.`program_id` WHERE `member`.`artist_panel_lid`='"+str(session['lid'])+"'"
    res=db.select(qry)

    return render_template('artist_panel/view_member.html',data=res)

@app.route('/view_member_post',methods=['post'])
def view_member_post():

    db=Db()
    search = request.form['textfield']
    qry="SELECT * FROM `member` WHERE `name` like '%"+search+"%' and `artist_panel_lid`='"+str(session['lid'])+"'"
    res=db.select(qry)
    return render_template('artist_panel/view_member.html',data=res)

@app.route('/delete_member/<id>')
def delete_member(id):
    d = Db()
    qry  = "DELETE FROM `member` WHERE `member_id`='"+str(id)+"'"
    rea = d.delete(qry)
    return "<script>alert('Deleted Succesfully');window.location='/view_member'</script>"



@app.route('/edit_member/<id>')
def edit_member(id):
    d = Db()
    qry = "SELECT * FROM `member` WHERE `member_id`='"+str(id)+"'"
    res = d.selectOne(qry)
    return render_template('artist_panel/edit_member.html', data=res,mid=id)

@app.route('/edit_member_post',methods=['post'])
def edit_member_post():

    db=Db()
    mid=request.form['h1']

    name = request.form['textfield']
    email = request.form['textfield2']
    phone = request.form['textfield3']
    gender = request.form['textfield6']
    place = request.form['textfield5']
    post = request.form['textfield7']
    district = request.form['textfield8']
    pincode = request.form['textfield9']
    if 'fileField' in request.files!="":
        photo = request.files['fileField']
        import time
        import datetime
        dt = time.strftime("%Y%m%d-%H%M%S")
        photo.save(staticpath +"member\\" +dt+".jpg")
        path = "/static/member/" + dt+".jpg"
        if photo.filename!="":
            qry = "UPDATE `member` SET `name`='"+name+"', `email`='"+email+"', `phone`='"+phone+"', `place`='"+place+"', `gender`='"+gender+"', `post`='"+post+"', `district`='"+district+"', `pincode`='"+pincode+"', `photo`='"+str(path)+"' where `member_id`='"+mid+"' "
            res=db.update(qry)
            return view_member()
        else:
            qry = "UPDATE `member` SET `name`='" + name + "', `email`='" + email + "', `phone`='" + phone + "', `place`='" + place + "', `gender`='" + gender + "', `post`='" + post + "', `district`='" + district + "', `pincode`='" + pincode + "' where `member_id`='" + mid + "' "
            res = db.update(qry)
            print("no photo1", qry)
            return view_member()
    else:
        qry = "UPDATE `member` SET `name`='" + name + "', `email`='" + email + "', `phone`='" + phone + "', `place`='" + place + "', `gender`='" + gender + "', `post`='" + post + "', `district`='" + district + "', `pincode`='" + pincode + "' where `member_id`='" + mid + "' "
        res = db.update(qry)
        print("no photo2", res)
        return view_member()


@app.route('/add_teamleader')
def add_teamleader():
    d = Db()
    qry = "SELECT * FROM `member` inner join category on category.program_id=member.program_id WHERE member.`artist_panel_lid`='"+str(session['lid'])+"'"
    res = d.select(qry)
    return render_template('artist_panel/add_teamleader.html', data=res)

@app.route('/add_teamleader_post', methods=['post'])
def add_teamleader_post():

     name = request.form['select']
     # category = request.form['textfield2']
     db=Db()
     qry = "INSERT INTO `team_leader`(`member_lid`,`panel_lid`) VALUES('"+str(name)+"','"+str(session['lid'])+"')"
     res = db.insert(qry)
     # qry ="INSERT INTO `team_leader` (`program_id`,`member_lid`) VALUES ('"+str(id)+"','"+str(session['lid'])+"')"
     qry1 = "update login set type='team leader' where login_id='"+str(name)+"'"
     res1 = db.update(qry1)
     return add_teamleader()

@app.route('/view_teamleader')
def view_teamleader():
    db=Db()
    # qry="SELECT * FROM `team_leader` WHERE `member_lid`='"+str(session['lid'])+"'"
    qry ="SELECT `team_leader`.*, `member`.`name`,`member`.`photo`, `category`.`program_name` FROM `member` INNER JOIN `team_leader` ON `team_leader`.`member_lid`=`member`.`member_lid` INNER JOIN `category` ON `category`.`program_id`=`member`.`program_id` WHERE `member`.`artist_panel_lid`='"+str(session['lid'])+"'"
    res=db.select(qry)
    return render_template('artist_panel/view_teamleader.html',data=res)

@app.route('/view_teamleader_post', methods=['post'])
def view_teamleader_post():
    db=Db()
    search = request.form['textfield']
    # qry="SELECT * FROM `team_leader` WHERE `member_lid`='"+str(session['lid'])+"'"
    qry ="SELECT `team_leader`.*, `member`.`name`,`member`.`photo`, `category`.`program_name` FROM `member` INNER JOIN `team_leader` ON `team_leader`.`member_lid`=`member`.`member_lid` INNER JOIN `category` ON `category`.`program_id`=`member`.`program_id` WHERE `member`.`artist_panel_lid`='"+str(session['lid'])+"' and member like '%"+search+"%'"
    res=db.select(qry)
    return render_template('artist_panel/view_teamleader.html',data=res)


@app.route('/delete_Tleader/<id>')
def delete_Tleader(id):
    db = Db()
    qry ="DELETE FROM `team_leader` WHERE `team_leader_id` ='"+str(id)+"'"
    res = db.delete(qry)
    return view_teamleader()

@app.route('/edit_teamleader/<id>')
def edit_teamleader(id):
    db = Db()
    qry ="SELECT `team_leader`.*, `member`.`name`,`member`.`photo`, `category`.`program_name` FROM `member` INNER JOIN `team_leader` ON `team_leader`.`member_lid`=`member`.`member_lid` INNER JOIN `category` ON `category`.`program_id`=`member`.`program_id` WHERE `team_leader`.`team_leader_id`='"+str(id)+"'"
    res = db.selectOne(qry)
    qry1 = "SELECT * FROM `member` inner join category on category.program_id=member.program_id WHERE member.`artist_panel_lid`='" + str(
        session['lid']) + "'"
    res1 = db.select(qry)
    return render_template('artist_panel/edit_teamleader.html',data=res,tl=res1)

@app.route('/edit_teamleader_post', methods=['post'])
def edit_teamleader_post():
    id = request.form['h1']
    name = request.form['select']
    db = Db()
    qry ="UPDATE `team_leader` SET `member_lid`='"+str(name)+"' WHERE `team_leader_id`='"+str(id)+"'"
    res = db.update(qry)
    return view_teamleader()







# @app.route('/view_teamleader_post',methods=['post'])
# def view_teamleader_post():
#
#     db=Db()
#     search = request.form['textfield']
#     qry="SELECT * FROM `member` WHERE `name` like '%"+search+"%' and `team_leader_lid`='"+str(session['lid'])+"'"
#     res=db.select(qry)
#     return render_template('artist_panel/view_teamleader.html',data=res)


# @app.route('/view_budget')
# def view_budget():
#     return render_template('artist_panel/view_budget.html')
#
# @app.route('/view_budget_post')
# def view_budget_post():
#     return render_template('artist_panel/view_budget.html')
#
# @app.route('/edit_budget')
# def edit_budget():
#     return render_template('artist_panel/edit_budget.html')
#
# @app.route('/edit_budget_post')
# def edit_budget_post():
#     return render_template('artist_panel/edit_budget.html')
#
#

@app.route('/add_highlight')
def add_highlight():
    d = Db()
    qry = "SELECT * FROM `category` WHERE `artist_panel_lid`= '"+str(session['lid'])+"'"
    res = d.select(qry)
    return render_template('artist_panel/add_highlight.html',data=res)

@app.route('/add_highlight_post', methods=['post'])
def add_highlight_post():
    prgrm = request.form['select']
    name = request.form['textfield']
    descrption = request.form['textarea']
    photo_01 = request.files['fileField']
    photo_02 = request.files['fileField2']

    photo_01.save(staticpath + "highlights\\" + photo_01.filename)
    path_01 = "/static/highlights/" + photo_01.filename
    photo_02.save(staticpath + "highlights\\" + photo_02.filename)
    path_02 = "/static/highlights/" + photo_02.filename

    db=Db()
    qry = "INSERT INTO `highlights` (`name`,`description`,`photo_1`,`photo_2`,`program_id`,`artist_panel_lid`) VALUES ('"+name+"','"+descrption+"','"+path_01+"', '"+path_02+"','"+prgrm+"','"+str(session['lid'])+"')"
    res = db.insert(qry)

    return render_template('artist_panel/add_highlight.html')

@app.route('/view_highlight')
def view_highlight():
    db=Db()
    qry = "SELECT `highlights`.*, `category`.`program_name` FROM `category` INNER JOIN `highlights` ON `highlights`.`program_id`=`category`.`program_id` WHERE `highlights`.`artist_panel_lid`='" + str(session['lid']) + "' "
    res = db.select(qry)
    return render_template('artist_panel/view_highlight.html',data=res)

@app.route('/view_highlight_post',methods=['post'])
def view_highlight_post():
    db = Db()
    name = request.form['search_field']
    qry ="SELECT `highlights`.*, `category`.`program_name` FROM `category` INNER JOIN `highlights` ON `highlights`.`program_id`=`category`.`program_id` WHERE `highlights`.`artist_panel_lid`='"+str(session['lid'])+"' and `category`.`program_name` like '%"+name+"%'"
    res = db.select(qry)
    return render_template('artist_panel/view_highlight.html',data=res)

@app.route('/delete_highlight/<id>')
def delete_highlight(id):
    d = Db()
    qry = "DELETE FROM `highlights` WHERE `highlight_id`='"+str(id)+"'"
    res = d.delete(qry)
    return '''<script>alert('Deleted');window.location='/view_highlight'</script>'''




@app.route('/edit_highlight/<id>')
def edit_highlight(id):
    d = Db()
    qry = "SELECT `highlights`.*, `category`.`program_name` FROM `category` INNER JOIN `highlights` ON `highlights`.`program_id`=`category`.`program_id` WHERE `highlight_id`='"+str(id)+"'"
    res = d.selectOne(qry)
    qry1 = "SELECT * FROM `category` WHERE `artist_panel_lid`= '"+str(session['lid'])+"'"
    res1 = d.select(qry1)
    return render_template('artist_panel/edit_highlight.html', data=res,data1=res1)

@app.route('/edit_highlight_post',methods=['post'])
def edit_highlight_post():
    prgrm = request.form['select']
    name = request.form['textfield']
    descrption = request.form['textarea']
    db = Db()
    if 'fileField' and 'fileField2' in request.files:
        photo_01 = request.files['fileField']
        photo_02 = request.files['fileField2']
        if photo_01.filename!="" and photo_02.filename!="":



            photo_01.save(staticpath + "highlights\\" + photo_01.filename)
            path_01 = "/static/highlights/" + photo_01.filename
            photo_02.save(staticpath + "highlights\\" + photo_02.filename)
            path_02 = "/static/highlights/" + photo_02.filename


            qry ="UPDATE `highlights` SET `name`='"+name+"', `description`='"+descrption+"', `photo_1`='"+path_01+"', `photo_2`='"+path_02+"', `program_id`='"+prgrm+"', `artist_panel_lid`='"+str(session['lid'])+"'"
            res = db.update(qry)

            return view_highlight()
        elif photo_01.filename!="":

            photo_01.save(staticpath + "highlights\\" + photo_01.filename)
            path_01 = "/static/highlights/" + photo_01.filename
            qry ="UPDATE `highlights` SET `name`='"+name+"', `description`='"+descrption+"', `photo_1`='"+path_01+"', `program_id`='"+prgrm+"', `artist_panel_lid`='"+str(session['lid'])+"'"
            res = db.update(qry)
            return view_highlight()
        elif photo_02.filename!="":

            photo_02.save(staticpath + "highlights\\" + photo_02.filename)
            path_02 = "/static/highlights/" + photo_02.filename
            qry = "UPDATE `highlights` SET `name`='" + name + "', `description`='" + descrption + "', `photo_2`='" + path_02 + "', `program_id`='" + prgrm + "', `artist_panel_lid`='" + str(session['lid']) + "'"
            res = db.update(qry)
            return view_highlight()
        else:
            qry = "UPDATE `highlights` SET `name`='" + name + "', `description`='" + descrption + "', `program_id`='" + prgrm + "', `artist_panel_lid`='" + str(session['lid']) + "'"
            res = db.update(qry)
            return view_highlight()
    else:
        qry = "UPDATE `highlights` SET `name`='" + name + "', `description`='" + descrption + "', `program_id`='" + prgrm + "', `artist_panel_lid`='" + str(session['lid']) + "'"
        res = db.update(qry)
        return view_highlight()


@app.route('/view_programme_reviews')
def view_programme_reviews():
    db=Db()
    qry="SELECT `review`.*,`user`.* FROM `review` JOIN `user` ON `user`.`login_id`=`review`.`user_lid`"
    res=db.select(qry)
    return render_template('artist_panel/view_programme_reviews.html',data=res)

@app.route('/search_programme_reviews_post',methods=['post'])
def search_programme_reviews_post():
    db=Db()
    search= request.form['textfield']
    search1=request.form['textfield1']
    qry="SELECT `review`.*,`user`.* FROM `review` JOIN `user` ON `user`.`login_id`=`review`.`user_lid`  WHERE `review`.`date` BETWEEN '"+search+"' and '"+search1+"'"
    print(qry)
    res=db.select(qry)
    print(res)
    return  render_template('artist_panel/view_programme_reviews.html',data=res)

@app.route('/view_booking_from_user')
def view_booking_from_user():
    db=Db()
    qry="SELECT `booking`.*,`user`.*,`category`.* FROM `booking` INNER JOIN `category` ON `category`.`program_id`=`booking`.`program_id` INNER JOIN `user` ON `user`.`login_id`=`booking`.`user_lid` WHERE `category`.`artist_panel_lid`='"+str(session['lid'])+"' and `booking`.`STATUS`='pending'"
    res=db.select(qry)
    return render_template('artist_panel/view_booking_from_user.html',data=res)

@app.route('/approve_booking/<id>')
def approve_booking(id):
    db=Db()
    qry2 = "UPDATE `booking` SET `status`='approved' WHERE `book_id`= '"+str(id)+"' "
    res = db.update(qry2)
    return view_booking_from_user()
@app.route('/reject_booking/<id>')
def reject_booking(id):
    db=Db()
    qry2 ="UPDATE `booking` SET `status`='rejected' WHERE `book_id`= '"+str(id)+"' "
    res =db.update(qry2)
    return view_booking_from_user()

@app.route('/approved_booking')
def approved_booking():
    db=Db()
    qry ="SELECT `booking`.*,`user`.*,`category`.* FROM `booking` INNER JOIN `category` ON `category`.`program_id`=`booking`.`program_id` INNER JOIN `user` ON `user`.`login_id`=`booking`.`user_lid` WHERE `category`.`artist_panel_lid`='"+str(session['lid'])+"' and `booking`.`STATUS`='approved'"
    res = db.select(qry)
    return render_template('artist_panel/approved_booking.html', data=res)

@app.route('/approved_booking_post', methods=['post'])
def approved_booking_post():
    s = request.form['textfield']
    s2 = request.form['textfield1']
    db = Db()
    qry = "SELECT `booking`.*,`user`.*,`category`.* FROM `booking` INNER JOIN `category` ON `category`.`program_id`=`booking`.`program_id` INNER JOIN `user` ON `user`.`login_id`=`booking`.`user_lid` WHERE `category`.`artist_panel_lid`='"+str(session['lid'])+"' AND `booking`.`STATUS`='approved' AND `booking`.`bdate` BETWEEN '"+s+"' AND '"+s2+"'"
    res = db.select(qry)
    print(qry)
    print(res)
    return render_template('artist_panel/approved_booking.html', data=res)

@app.route('/rejected_booking')
def rejected_booking():
    db=Db()
    qry ="SELECT `booking`.*,`user`.*,`category`.* FROM `booking` INNER JOIN `category` ON `category`.`program_id`=`booking`.`program_id` INNER JOIN `user` ON `user`.`login_id`=`booking`.`user_lid` WHERE `category`.`artist_panel_lid`='"+str(session['lid'])+"' and `booking`.`STATUS`='rejected'"
    res = db.select(qry)
    print(res)
    return render_template('artist_panel/rejected_booking.html', data=res)

@app.route('/rejected_booking_post', methods=['post'])
def rejected_booking_post():
    s = request.form['textfield']
    s2 = request.form['textfield1']
    db = Db()
    qry = "SELECT `booking`.*,`user`.*,`category`.* FROM `booking` INNER JOIN `category` ON `category`.`program_id`=`booking`.`program_id` INNER JOIN `user` ON `user`.`login_id`=`booking`.`user_lid` WHERE `category`.`artist_panel_lid`='"+str(session['lid'])+"' AND `booking`.`STATUS`='rejected' AND `booking`.`bdate` BETWEEN '"+s+"' AND '"+s2+"'"
    res = db.select(qry)
    return render_template('artist_panel/rejected_booking.html', data=res)

@app.route('/view_payment/<id>')
def view_payment(id):
    db=Db()
    qry = "SELECT * FROM `payment` where `book_id`='"+str(id)+"'"
    res = db.selectOne(qry)
    print(res)
    return render_template('artist_panel/view_payment.html',data=res)


@app.route('/artist_paswrd')
def artist_paswrd():
    return render_template('artist_panel/change_paswrd.html')

@app.route('/artist_pswrd_post', methods=['post'])
def artist_pswrd_post():
    op = request.form['p1']
    np = request.form['p2']
    cnp = request.form['p3']
    db = Db()
    qry = "SELECT * FROM `login` WHERE `password`='"+op+"'"
    res = db.selectOne(qry)
    if res is not None:
        if np==cnp:
            qry = "UPDATE `login` SET `password`='"+cnp+"' where login_id='"+str(session['lid'])+"' "
            res = db.update(qry)
            return redirect('/login')
        else:
            return '''<script>alert('Invalid');window.location='/artist_paswrd'</script>'''
    else:
        return '''<script>alert('Invalid');window.location='/artist_paswrd'</script>'''



################android methods


@app.route("/and_userreg",methods=['post'])
def and_userreg():
    name=request.form["name"]
    email=request.form["email"]
    place=request.form["place"]
    phone=request.form["phone"]
    post=request.form["post"]
    district=request.form["district"]
    pincode=request.form["pincode"]
    photo=request.form["photo"]
    password=request.form["password"]

    import time
    dt = time.strftime("%Y%m%d_%H%M%S")
    # photo.save(staticpath + "user\\" + dt + ".jpg")
    path = "/static/user/" + dt + ".jpg"

    import base64
    with open(staticpath + "user\\" + dt + ".jpg",mode="wb") as h:
        h.write(base64.b64decode(photo))

    qry="INSERT INTO `login` (`username`,`password`,`type`) VALUES ('"+email+"','"+password+"','user')"
    db=Db()
    id=db.insert(qry)
    qry2="INSERT INTO `user` (`name`,`email`,`phone`,`place`,`post`,`district`,`pincode`,`photo`,login_id) VALUES ('"+name+"','"+email+"','"+phone+"','"+place+"','"+post+"','"+district+"','"+pincode+"','"+path+"','"+str(id)+"')"
    db.insert(qry2)
    return jsonify(status='ok')

@app.route('/and_send_app_feedback',methods=['post'])
def and_send_app_feedback():
    feedback=request.form['feedback']

    user_lid=request.form['user_lid']
    rating=request.form['rating']
    db=Db()
    qry="INSERT INTO `feedback`(`feedback`,`date`,`user_lid`,`rating`) VALUES ('"+feedback+"',curdate(),'"+user_lid+"','"+rating+"')"
    db.insert(qry)
    return jsonify(status='ok')

@app.route('/and_edit_profile',methods=['post'])
def and_edit_profile():
    name = request.form["name"]
    email = request.form["email"]
    place = request.form["place"]
    phone = request.form["phone"]
    post = request.form["post"]
    district = request.form["district"]
    pincode = request.form["pincode"]
    photo = request.form["photo"]
    user_lid = request.form['user_lid']
    db=Db()
    if 'image' in request.files:
        image = request.files['photo']
        import time
        dt = time.strftime("%Y%m%d_%H%M%S")
        image.save(staticpath + "user\\" + dt + ".jpg")
        path = "/static/user/" + dt + ".jpg"
        qry="update `user` set `name`='"+name+"',`email`='"+email+"',`phone`='"+phone+"',`place`='"+place+"',`post`='"+post+"',`district`='"+district+"',`pincode`='"+pincode+"',`photo`='"+str(path)+"' where login_id='"+user_lid+"'"
        res=db.update(qry)
    else:
        qry1="update `user` set `name`='"+name+"',`email`='"+email+"',`phone`='"+phone+"',`place`='"+place+"',`post`='"+post+"',`district`='"+district+"',`pincode`='"+pincode+"' where login_id='"+user_lid+"'"
        res=db.update(qry1)
        return jsonify(status='ok')

@app.route('/and_login_post',methods=['post'])
def and_login_post():
    username = request.form['username']
    password = request.form['password']
    db = Db()
    res = db.selectOne("SELECT * FROM login WHERE `username`='" + username + "' AND `password`='" + password + "'")
    if res is not None:
        return jsonify(status='ok',lid=res['login_id'],type=res['type'])
    else:
        return jsonify(status='no')


@app.route('/and_user_profile',methods=['post'])
def and_user_profile():
    db=Db()
    lid=request.form["lid"]
    qry="SELECT * FROM `user` WHERE `login_id`='"+lid+"'"
    res= db.selectOne(qry)
    return jsonify(status='ok',name=res['name'],email=res['email'],phone=res['phone'],place=res['place'],post=res['post'],district=res['district'],pincode=res['pincode'],photo=res['photo'])

@app.route('/and_user_view_artistpanel_nearby_location',methods=['post'])
def and_user_view_artistpanel_nearby_location():
    db=Db()
    qry="SELECT `panel_id`,`login_id`,`name`,`email`,`phone`,`team_leader`.`member_lid`,`place`,`post`,`district`,`pincode`,`logo`,`latitude`,`longitude`,`status`, DATE_FORMAT(`est_year`,'%d-%m-%y') as `est_year` FROM `artist_panel` inner join `team_leader` on `team_leader`.`panel_lid`=`artist_panel`.`login_id`"
    data=db.select(qry)
    return jsonify(status='ok',data=data)

@app.route('/and_user_view_artistpanel_nearby_location_search',methods=['post'])
def and_user_view_artistpanel_nearby_location_search():
    search=request.form["search"]
    db=Db()
    qry="SELECT `panel_id`,`login_id`,`name`,`email`,`phone`,`place`,`team_leader`.`member_lid`,`post`,`district`,`pincode`,`logo`,`latitude`,`longitude`,`status`, DATE_FORMAT(`est_year`,'%d-%m-%y') as `est_year`  inner join `team_leader` on `team_leader`.`panel_lid`=`artist_panel`.`login_id` FROM `artist_panel` where district like '%"+search+"%'"
    data=db.select(qry)
    return jsonify(status='ok',data=data)

@app.route('/and_user_categories',methods=['post'])
def and_user_categories():
    db=Db()
    qry="SELECT * FROM `category`"
    data=db.select(qry)
    return jsonify(status='ok',data=data)


@app.route('/and_user_categories_search',methods=['post'])
def and_user_categories_search():
    search=request.form["search"]
    db=Db()
    qry="SELECT * FROM `category` where program_name like '%"+search+"%'"
    data=db.select(qry)
    return jsonify(status='ok',data=data)


@app.route('/and_user_highlights',methods=['post'])
def and_user_highlights():
    db=Db()
    qry="SELECT * FROM `highlights`"
    data=db.select(qry)
    return jsonify(status='ok',data=data)

@app.route('/and_user_highlights_search',methods=['post'])
def and_user_highlights_search():
    search=request.form["search"]
    db=Db()
    qry="SELECT * FROM `highlights` where name like '%"+search+"%'"
    data=db.select(qry)
    return jsonify(status='ok',data=data)


@app.route('/and_view_members',methods=['post'])
def and_view_members():
    db=Db()
    qry="SELECT * FROM `member`"
    data=db.select(qry)
    return jsonify(status='ok',data=data)

@app.route('/and_view_members_search',methods=['post'])
def and_view_members_search():
    search=request.form["search"]
    db=Db()
    qry="SELECT * FROM `member` where name like '%"+search+"%'"
    data=db.select(qry)
    return jsonify(status='ok',data=data)


@app.route('/and_tl_profile',methods=['post'])
def and_tl_profile():
    db=Db()
    lid=request.form["lid"]
    qry="SELECT * FROM `team_leader` INNER JOIN `member` ON `team_leader`.`member_lid`=`member`.`member_lid` WHERE `team_leader`.`member_lid`='"+lid+"'"
    res= db.selectOne(qry)
    print(qry)

    return jsonify(status='ok',name=res['name'],email=res['email'],phone=res['phone'],place=res['place'],post=res['post'],district=res['district'],pincode=res['pincode'],photo=res['photo'],gender=res['gender'])



@app.route('/and_book_a_program',methods=['post'])
def and_book_a_program():
    db=Db()
    # bookid=request.form['book_id']
    bdate=request.form['bdate']
    program_id=request.form['pgid']
    location=request.form['location']
    user_lid=request.form['lid']
    qry="INSERT INTO `booking` (`date`,`user_lid`,`program_id`,`bdate`,`location`,`status`) VALUES (curdate(),'"+user_lid+"','"+program_id+"','"+bdate+"','"+location+"','pending')"
    res=db.insert(qry)
    return jsonify(status='ok')



@app.route('/and_tl_categories',methods=['post'])
def and_tl_categories():
    db=Db()
    qry="SELECT * FROM `category`"
    data=db.select(qry)
    return jsonify(status='ok',data=data)

@app.route('/and_tl_categories_search',methods=['post'])
def and_tl_categories_search():
    search=request.form["search"]
    db=Db()
    qry="SELECT * FROM `category` where program_name like '%"+search+"%'"
    data=db.select(qry)
    return jsonify(status='ok',data=data)


@app.route('/and_tl_view_members',methods=['post'])
def and_tl_view_members():
    db=Db()
    qry="SELECT * FROM `member`"
    data=db.select(qry)
    return jsonify(status='ok',data=data)

@app.route('/and_tl_view_members_search',methods=['post'])
def and_tl_view_members_search():
    search=request.form["search"]
    db=Db()
    qry="SELECT * FROM `member` where name like '%"+search+"%'"
    data=db.select(qry)
    return jsonify(status='ok',data=data)

@app.route('/and_tl_highlights',methods=['post'])
def and_tl_highlights():
    db=Db()
    qry="SELECT * FROM `highlights`"
    data=db.select(qry)
    return jsonify(status='ok',data=data)

@app.route('/and_tl_highlights_search',methods=['post'])
def and_tl_highlights_search():
    search=request.form["search"]
    db=Db()
    qry="SELECT * FROM `highlights` where name like '%"+search+"%'"
    data = db.select(qry)
    return jsonify(status='ok',data=data)


@app.route('/and_tl_view_bookings',methods=['post'])
def and_tl_view_bookings():
    db=Db()
    qry="SELECT `book_id`,DATE_FORMAT(`date`,'%d-%m-%y') as date,`user_lid`,booking.`program_id`,`status`, DATE_FORMAT(`bdate`,'%d-%m-%y') as bdate ,`location`,`program_name`,user.`photo`,`artist_panel_lid`,`description`,`budget`,user.name,user.email,user.phone,user.place,user.post,user.district FROM  booking INNER JOIN `category` ON `booking`.`program_id`=`category`.`program_id` INNER JOIN user ON `user`.`login_id`=`booking`.`user_lid` WHERE status='Pending'"
    data=db.select(qry)
    return jsonify(status='ok',data=data)

@app.route('/and_tl_view_booking_confirmed',methods=['post'])
def and_tl_view_booking_confirmed():
    db=Db()
    qry="SELECT `book_id`,DATE_FORMAT(`date`,'%d-%m-%y') as date,`user_lid`,booking.`program_id`,`status`, DATE_FORMAT(`bdate`,'%d-%m-%y') as bdate ,`location`,`program_name`,user.`photo`,`artist_panel_lid`,`description`,`budget`,user.name,user.email,user.phone,user.place,user.post,user.district FROM  booking INNER JOIN `category` ON `booking`.`program_id`=`category`.`program_id` INNER JOIN user ON `user`.`login_id`=`booking`.`user_lid` WHERE  status='Approved'"
    data=db.select(qry)
    return jsonify(status='ok',data=data)

@app.route('/and_tl_view_booking_rejected',methods=['post'])
def and_tl_view_booking_rejected():
    db=Db()
    qry="SELECT `book_id`,DATE_FORMAT(`date`,'%d-%m-%y') as date,`user_lid`,booking.`program_id`,`status`, DATE_FORMAT(`bdate`,'%d-%m-%y') as bdate ,`location`,`program_name`,user.`photo`,`artist_panel_lid`,`description`,`budget`,user.name,user.email,user.phone,user.place,user.post,user.district FROM  booking INNER JOIN `category` ON `booking`.`program_id`=`category`.`program_id` INNER JOIN user ON `user`.`login_id`=`booking`.`user_lid` WHERE  status='Rejected'"
    data=db.select(qry)
    return jsonify(status='ok',data=data)

@app.route('/and_tl_approve_booking',methods=['post'])
def and_tl_approve_booking():
    bid=request.form['bid']
    db=Db()
    qry="UPDATE `booking` SET `status`='Approved' WHERE `book_id`='"+bid+"'"
    res=db.update(qry)
    return jsonify(status='ok')

@app.route('/and_tl_reject_booking',methods=['post'])
def and_tl_reject_booking():
    bid=request.form['bid']
    db=Db()
    qry = "UPDATE `booking` SET `status`='Rejected' WHERE `book_id`='" + bid + "'"
    res = db.update(qry)
    return jsonify(status='ok')

@app.route('/and_user_view_booking',methods=['post'])
def and_user_view_booking():
    db=Db()
    lid=request.form['lid']
    qry="SELECT `book_id`,`date`,`user_lid`,booking.`program_id`,`status`, DATE_FORMAT(`bdate`,'%d-%m-%y') as bdate ,`location`,`program_name`,`photo`,`artist_panel_lid`,`description`,`budget`  FROM  booking INNER JOIN `category` ON `booking`.`program_id`=`category`.`program_id`  WHERE booking.user_lid='"+lid+"'"
    res=db.select(qry)
    return jsonify(status='ok',data=res)

@app.route('/and_tl_reviews',methods=['post'])
def and_tl_reviews():
    pid=request.form['pid']
    lid=request.form['lid']
    db=Db()
    qry = "SELECT `review`.*, DATE_FORMAT(review.`date`,'%d-%m-%y') AS rDATE, `user`.*, `category`.`program_name` FROM `review` INNER JOIN `user` ON `review`.`user_lid`=`user`.`login_id` INNER JOIN `category` ON `category`.`program_id`=`review`.`program_id` where review.`program_id`='"+pid+"'"
    # qry = "SELECT `review`.*, `user`.*, `category`.`program_name` FROM `review` INNER JOIN `user` ON `review`.`user_lid`=`user`.`login_id` INNER JOIN `category` ON `category`.`program_id`=`review`.`program_id`  where review.`program_id`='"+pid+"'"
    # qry="SELECT * FROM `review` INNER JOIN `user` ON `review`.`user_lid`=`user`.`login_id`  INNER JOIN `category` ON `category`.`program_id`=`review`.`program_id` where review.`program_id`='"+pid+"'"
    res=db.select(qry)
    return jsonify(status='ok',data=res)

@app.route('/and_user_send_review',methods=['post'])
def and_user_send_review():
    review=request.form['review']
    program_id=request.form['pgmid']
    print(program_id)
    user_lid=request.form['lid']
    db=Db()
    qry="INSERT INTO `review` (`review`,`date`,`program_id`,`user_lid`) VALUES ('"+review+"',curdate(),'"+program_id+"','"+user_lid+"')"
    res=db.insert(qry)
    return jsonify(status='ok',data=res)

@app.route('/and_user_view_review',methods=['post'])
def and_user_view_review():
    user_lid=request.form['lid']
    db=Db()
    qry="SELECT category.program_name,photo,name, `review_id`,`review`,DATE_FORMAT(`date`,'%d-%m-%y') as date, review.program_id,user_lid FROM `review` INNER JOIN `category` ON `review`.`program_id`=`category`.`program_id` INNER JOIN `artist_panel` ON `category`.`artist_panel_lid`=`artist_panel`.`login_id` WHERE `user_lid`='"+user_lid+"'"
    res=db.select(qry)
    return jsonify(status='ok',data=res)

@app.route('/and_chng_pswrd',methods=['post'])
def and_chng_pswrd():

    lid=request.form['lid']
    current_password = request.form['current']
    new_password = request.form['new']
    confirm_password = request.form['confirm']
    db = Db()
    qry="SELECT * FROM login WHERE  `password`='" + current_password + "' and login_id='"+lid+"'"
    res = db.selectOne(qry)
    if res is not None:
        if new_password==confirm_password:
            qry1="UPDATE `login` SET `password`='"+new_password+"' where login_id='"+lid+"'"
            res1=db.update(qry1)
            return jsonify(status='ok')
        else:
            return jsonify(status='no')
    else:
        return jsonify(status='none')


@app.route('/and_chng_pswrd_tl',methods=['post'])
def and_chng_pswrd_tl():
    lid = request.form['lid']
    current_password = request.form['current']
    new_password = request.form['new']
    confirm_password = request.form['confirm']
    db = Db()
    qry = "SELECT * FROM login WHERE  `password`='" + current_password + "' and login_id='" + lid + "'"
    res = db.selectOne(qry)
    if res is not None:
        if new_password == confirm_password:
            qry1 = "UPDATE `login` SET `password`='" + new_password + "' where login_id='" + lid + "'"
            res1 = db.update(qry1)
            return jsonify(status='ok')
        else:
            return jsonify(status='no')
    else:
        return jsonify(status='none')


@app.route('/and_message_chat',methods=['post'])
def and_message_chat():
    from_id=request.form['fromid']
    to_id=request.form['toid']
    message=request.form['message']
    db=Db()
    qry="INSERT INTO `chat` (`from_id`,`to_id`,`date`,`message`) VALUES ('"+from_id+"','"+to_id+"',curdate(),'"+message+"')"
    res=db.insert(qry)
    return jsonify(status='ok',data=res)


@app.route('/and_view_message',methods=['post'])
def and_view_message():
    from_id = request.form['fromid']
    to_id = request.form['toid']
    chatid = request.form['chatid']
    db=Db()
    qry="SELECT * FROM `chat` WHERE ((from_id='"+from_id+"' and to_id='"+to_id+"') or (from_id='"+to_id+"' and to_id='"+from_id+"')) and chat_id>"+ chatid+" order by chat_id "
    print(qry)
    res=db.select(qry)
    return jsonify(status='ok',data=res)


@app.route('/and_tl_view_users',methods=['post'])
def and_tl_view_users():
    db=Db()
    qry="SELECT * FROM `user`"
    data=db.select(qry)
    return jsonify(status='ok',data=data)


@app.route('/and_add_payment',methods=['post'])
def and_add_payment():
    db=Db()
    bid = request.form['book_id']
    lid=request.form['lid']
    accno=request.form['acnt_no']
    amnt = request.form['amnt']
    cvv=request.form['cvv']
    bank_name=request.form['bname']
    qry = "INSERT INTO `payment`(`date`,`account_no`,`cvv`,`book_id`,`bank_name`,`status`,`amount`) VALUES(CURDATE(),'"+accno+"','"+cvv+"','"+bid+"','"+bank_name+"','Paid','"+amnt+"')"
    res=db.insert(qry)
    return jsonify(status='ok',data=res)



if __name__ == '__main__':
    app.run(port=1234, debug=True,host="0.0.0.0")
