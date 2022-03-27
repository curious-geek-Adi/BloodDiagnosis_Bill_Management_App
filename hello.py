from flask import Flask,render_template,redirect,request,url_for,flash,session,abort
import hello_db
import one
app=Flask(__name__)
app.config['SECRET_KEY']='thisissecretkey'

@app.errorhandler(404)
def path_error(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_error(obj):
    return render_template("500.html"),500

@app.route('/')
def index_view():
    flash('Hey Buddy,Welcome to Registraion Page','welcome')
    list=hello_db.testlist()
    msg=[]
    code=one.uniquecode()
    cid=code[11:]
    for x in list:
        msg.append(x)

    list1=hello_db.fulldata_cont()
    contr=[]
    for x in list1:
        contr.append(x)

    return render_template("newhome.html",msg=msg,cid=cid,contr=contr);




@app.route('/register/<gid>/',methods=['GET','POST'])
def register_view(gid):
    if request.method=='POST':
        data={}

        if(100<= int(request.form["age"])):
            return redirect(url_for("fail"))
        # f1=request.form["first"]
        # if((f1.isalnum()==True) or (True==f1.isnumeric())):
        #     abort(401,"Sorry You are entered Wrong Value in First Name");

        # f1=request.form["last"]
        # if((f1.isalnum()==True) or (True==f1.isnumeric())):
        #     abort(501,"Sorry You are enter numeric Value in Last Name");

        data["cid"]=gid
        temp=request.form["test_name"]
        temp2=temp.split("|")
        look=request.form['contr']
        look1=look.split("|")
        data["first_name"]=request.form['first']
        data["last_name"] = request.form['last']
        data["gender"] = request.form['gender']
        data["contr"] =look1[0]
        data["contr_id"]=look1[1]
        data["age"]=request.form['age']
        data["test_name"]=temp2[0]
        data["test_price"]=temp2[1]
        hello_db.savedata(data)
        temp=hello_db.fulldata()
        data=[]
        for x in temp:
            data.append(x)
        #msg=[cid,first,last,age,price,test]
        # data[cid]=[]
        # data[cid].append(msg)
        # print(data)
        flash('Yay..!! Registration successfully','success')
        #return render_template("info.html",data=data);
        return redirect(url_for('index_view'))
    elif request.method=='GET':
        temp=hello_db.fulldata()
        data=[]
        for x in temp:
            data.append(x)
    return render_template("info.html",data=data);

@app.route('/showlist')
def showlist():
    if request.method=='GET':
        temp=hello_db.fulldata()
        data=[]
        for x in temp:
            data.append(x)
    return render_template("info.html",data=data);




@app.route('/search')
def search():
    temp=hello_db.countall_list()
    count=[]
    for x in temp:
        count.append(x)

    cost=[]
    temp2=hello_db.total_cost()
    for x in temp2:
        cost.append(x)
    print("Temp2 is <><><><>",temp2)
    print("COST is<><><><>",cost)
    # temp3=hello_db.search_record(name)
    # record=[]
    # for x in temp3:
    #     record.append(x)
    numdoc=0
    f_cost=0
    list1=hello_db.fulldata_cont()
    contr=[]
    for x in list1:
        contr.append(x)
    return render_template("search.html",count=count,contr=contr,cost=cost,numdoc=numdoc,f_cost=f_cost)

@app.route('/fail')
def fail():
    session.pop('SECRET_KEY', None)
    flash('Sorry!.. Your Age limit is crossed','error')
    return render_template("fail.html",msg=" Registrain Failed...")

#delete at all list
@app.route("/delete/<cid>/")
def delete(cid):
    hello_db.deletecoll(cid)
    return redirect(url_for('showlist'))

    #delte at search list
@app.route("/del/<cid>/<name>/",methods=["post"])
def delete_search(cid,name):
    hello_db.deletecoll(cid)
    return redirect(url_for('search_name',nm=name))

@app.route('/searchname',methods=["POST"])
def searchname():
    #under lin code retrive contractor info and display to search page
    temp=hello_db.countall_list()
    count=[]
    for x in temp:
        count.append(x)
#here retivr the selected contractor and find data accordn to that only
    name=request.form["contr"]
    temp3=hello_db.search_record(name)
    record=[]
    for x in temp3:
        record.append(x)

    numdoc=len(record)# basically count how many filter document
    print("<><><>>><<record llok like",record)
    fcost=[]
    for ele in record:
        fcost.append(ele["test_price"])

    f_cost=0
    for x in fcost:
        f_cost=f_cost+float(x)

    list1=hello_db.fulldata_cont()
    contr=[]
    for x in list1:
        contr.append(x)

    cost=[]
    temp2=hello_db.total_cost()
    for x in temp2:
        cost.append(x)
    return render_template("search.html",record=record,contr=contr,count=count,cost=cost,numdoc=numdoc,f_cost=f_cost)

# later work on search based on age
@app.route('/searchage',methods=["POST"])
def searchage():
    #under lin code retrive contractor info and display to search page
    temp=hello_db.countall_list()
    count=[]
    for x in temp:
        count.append(x)
#here retivr the selected contractor and find data accordn to that only
    name=request.form["contr"]
    temp3=hello_db.search_record(name)
    record=[]
    for x in temp3:
        record.append(x)

    numdoc=len(record)# basically count how many filter document
    print("<><><>>><<record llok like",record)
    fcost=[]
    for ele in record:
        fcost.append(ele["test_price"])

    f_cost=0
    for x in fcost:
        f_cost=f_cost+float(x)

    list1=hello_db.fulldata_cont()
    contr=[]
    for x in list1:
        contr.append(x)

    cost=[]
    temp2=hello_db.total_cost()
    for x in temp2:
        cost.append(x)
    return render_template("search.html",record=record,contr=contr,count=count,cost=cost,numdoc=numdoc,f_cost=f_cost)


@app.route('/search_name/<nm>',methods=["POST","GET"])
def search_name(nm):
    #under lin code retrive contractor info and display to search page
    temp=hello_db.countall_list()
    count=[]
    for x in temp:
        count.append(x)
#here retivr the selected contractor and find data accordn to that only
    name=nm;
    #request.form["contr"]
    temp3=hello_db.search_record(name)
    record=[]
    for x in temp3:
        record.append(x)

    numdoc=len(record)# basically count how many filter document
    print("<><><>>><<record llok like",record)
    fcost=[]
    for ele in record:
        fcost.append(ele["test_price"])

    f_cost=0
    for x in fcost:
        f_cost=f_cost+float(x)

    list1=hello_db.fulldata_cont()
    contr=[]
    for x in list1:
        contr.append(x)

    cost=[]
    temp2=hello_db.total_cost()
    for x in temp2:
        cost.append(x)
    return render_template("search.html",record=record,contr=contr,count=count,cost=cost,numdoc=numdoc,f_cost=f_cost)



# new login features
@app.route('/signup_user')
