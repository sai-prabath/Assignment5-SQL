from TicketBookingSystem.app.TicketBookingSystem import TicketBookingSystem
from TicketBookingSystem.util.dbutil import DBUtil

db_conn = DBUtil.getDBConn()
ticket_booking_system = TicketBookingSystem(db_conn)
ticket_booking_system.run()



