from flask import flash, request
from .models import Event1, Event2, Event3, Event4, Event5, Event6, Event7, Event8, Event9
from . import db




def techget(name, dept, ieee, email, tech_teamname, tech_memember, techis, event1, event2, event3, event4, event5, rollno):

    result = ' '

    a = []
    if techis == '1':
        if event1 == 'on':
            a.append('Event 1')
            roll = Event1.query.filter_by(rollno=rollno).first()
            if roll is None:
                my_list = a
                result = ','.join(my_list)
                # print("TECH Result::",result)
                new_reg = Event1(name=name, rollno=rollno, dept=dept, ieee=ieee, 
                                 email=email, event=result, teamname=tech_teamname, team_members=tech_memember)
                db.session.add(new_reg)
                db.session.commit()
            else:
                flash("You already registered for this event")
        if event2 == 'on':
            a.append('Event2')
            roll = Event2.query.filter_by(rollno=rollno).first()
            if roll is None:
                my_list = a
                result = ','.join(my_list)
                # print("TECH Result::",result)
                new_reg = Event2(name=name, rollno=rollno, dept=dept, ieee=ieee, 
                                 email=email, event=result, teamname=tech_teamname, team_members=tech_memember)
                db.session.add(new_reg)
                db.session.commit()
            else:
                flash("You already registered for this event")
        if event3 == 'on':
            a.append('Event 3')
            roll = Event3.query.filter_by(rollno=rollno).first()
            if roll is None:
                my_list = a
                result = ','.join(my_list)
                # print("TECH Result::",result)
                new_reg = Event3(name=name, rollno=rollno, dept=dept, ieee=ieee, 
                                 email=email, event=result, teamname=tech_teamname, team_members=tech_memember)
                db.session.add(new_reg)
                db.session.commit()
            else:
                flash("You already registered for this event")
        if event4 == 'on':
            a.append('Event 4')
            roll = Event4.query.filter_by(rollno=rollno).first()
            if roll is None:
                my_list = a
                result = ','.join(my_list)
                # print("TECH Result::",result)
                new_reg = Event4(name=name, rollno=rollno, dept=dept, ieee=ieee, 
                                 email=email, event=result, teamname=tech_teamname, team_members=tech_memember)
                db.session.add(new_reg)
                db.session.commit()
            else:
                flash("You already registered for this event")
            a.append('DESTINATION JUNCTION')
        if event5 == 'on':
            a.append('Event 5')
            roll = Event5.query.filter_by(rollno=rollno).first()
            if roll is None:
                my_list = a
                result = ','.join(my_list)
                # print("TECH Result::",result)
                new_reg = Event5(name=name, rollno=rollno, dept=dept, ieee=ieee, 
                                 email=email, event=result, teamname=tech_teamname, team_members=tech_memember)
                db.session.add(new_reg)
                db.session.commit()
            else:
                flash("You already registered for this event")



    a.clear()
    return result


def nontechget(name, dept, ieee,  email, nontech_teamname, nontech_memember, nontechis, event6, event7, event8, event9, rollno):
    nontech_result = ' '
    a = []
    if nontechis == '1':

        if event6 == 'on':
            a.append('Event6')
            roll = Event6.query.filter_by(rollno=rollno).first()
            if roll is None:
                nontech_list = a
                nontech_result = ','.join(nontech_list)
                # print("TECH Result::",result)
                new_reg = Event6(name=name, rollno=rollno, dept=dept, ieee=ieee,  email=email,
                                 event=nontech_result, teamname=nontech_teamname, team_members=nontech_memember)
                db.session.add(new_reg)
                db.session.commit()
            else:
                flash("You already registered for this event")
        if event7 == 'on':
            a.append('Event 7')
            roll = Event7.query.filter_by(rollno=rollno).first()
            if roll is None:
                nontech_list = a
                nontech_result = ','.join(nontech_list)
                # print("TECH Result::",result)
                new_reg = Event7(name=name, rollno=rollno, dept=dept, ieee=ieee,  email=email,
                                 event=nontech_result, teamname=nontech_teamname, team_members=nontech_memember)
                db.session.add(new_reg)
                db.session.commit()
            else:
                flash("You already registered for this event")
        if event8 == 'on':
            a.append('Event 8')
            roll = Event1.query.filter_by(rollno=rollno).first()
            if roll is None:
                nontech_list = a
                nontech_result = ','.join(nontech_list)
                # print("TECH Result::",result)
                new_reg = Event1(name=name, rollno=rollno, dept=dept, ieee=ieee,  email=email,
                                 event=nontech_result, teamname=nontech_teamname, team_members=nontech_memember)
                db.session.add(new_reg)
                db.session.commit()
            else:
                flash("You already registered for this event")
        if event9 == 'on':

            a.append('Event 9')
            roll = Event9.query.filter_by(rollno=rollno).first()
            if roll is None:
                nontech_list = a
                nontech_result = ','.join(nontech_list)
                # print("TECH Result::",result)
                new_reg = Event9(name=name, rollno=rollno, dept=dept, ieee=ieee,  email=email,
                                 event=nontech_result, teamname=nontech_teamname, team_members=nontech_memember)
                db.session.add(new_reg)
                db.session.commit()
            else:
                flash("You already registered for this event")
    a.clear()
    return nontech_result
