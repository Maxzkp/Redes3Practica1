from SNMPdata import MonitorInfo
import os

class Menu:

	def __init__(self, file = 'hosts.txt'):
		self.file = file
		self.monitor = MonitorInfo()
		if os.path.exists(self.file):
			self.monitor.readFile(self.file)
		self.state = 0
		self.observingHost = None
		self.changes = False
		while 1:
			os.system('clear')
			print('Control del monitoreo')
			print(f'Version de SNMP: {self.monitor.SNMPv}')
			print(f'Puerto: {self.monitor.port}')
			print(f'Nombre de Comunidad: {self.monitor.comunity}')
			print(f'{len(self.monitor.hosts)} hosts monitoreados')
			if self.changes:
				print('*Cambios sin guardar*')

			if self.state == 0:
				self.menuPrincipal()
			elif self.state == 1:
				self.menuHosts()
			elif self.state == 2:
				self.menuHost()

	def menuPrincipal(self):
		print('\nMenu\n')
		print('1) Modificar version de SNMP')
		print('2) Modificar puerto')
		print('3) Modificar nombre de comunidad')
		print('4) Ver hosts')
		print('5) Guardar cambios')
		if self.changes:
			print('6) Restaurar cambios')
		print('q) Salir')
		opt = input('\n\nSeleccione una opcion y pulse enter: ')
		if opt == '1':
			self.monitor.SNMPv = input('Ingrese la version de SNMP: ')
			self.changes = True
		elif opt == '2':
			self.monitor.port = input('Ingrese El puesto: ')
			self.changes = True
		elif opt == '3':
			self.monitor.comunity = input('Ingrese el nombre de la comunidad: ')
			self.changes = True
		elif opt == '4':
			self.state = 1
		elif opt == '5':
			self.monitor.saveFile(self.file)
			self.changes = False
		elif opt == '6':
			if os.path.exists(self.file):
				self.monitor.readFile(self.file)
			else:
				self.monitor = MonitorInfo()
			self.changes = False
		elif opt == 'q':
			exit()

	def menuHosts(self):
		optNum = 1
		print('\nHosts\n')
		if len(self.monitor.hosts) > 0:
			print('(Seleccione un host para ver mas opciones)')
			for host in self.monitor.hosts:
				print(f'{optNum}) {host}')
				optNum += 1
		print(f'{optNum}) Nuevo Host')
		print(f'{optNum + 1}) Volver')
		opt = input('\n\nSeleccione una opcion y pulse enter: ')
		
		if opt == str(1 + len(self.monitor.hosts)):
			newHost = input('Ingrese la ip del nuevo host: ')
			self.monitor.addHost(newHost)
			self.changes = True
		elif opt == str(2 + len(self.monitor.hosts)):
			self.state = 0
		else:
			self.observingHost = self.monitor.hosts[int(opt)-1]
			self.state = 3
			

	def menuHost(self):
		print(f'\nHost {self.observingHost}\n')
		print('1) Eliminar host')
		print('2) Generar reporte')
		opt = input('\n\nSeleccione una opcion y pulse enter: ')
		if opt == '1':
			confirm = input('Seguro que desea eliminar este host? (y/n):')
			if confirm == 'y':
				self.monitor.removeHost(self.observingHost)
				self.observingHost = None
				self.state = 2
				self.changes = True
		elif opt == '2':
			self.observingHost = None
			self.state = 2
		
Menu()