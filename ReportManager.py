from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
w, h = A4

def makeReport(monitor, target):
	c = canvas.Canvas(f'rrd/{target} report.pdf')
	c.drawImage(f'{monitor.systemGet(target)}.jpg', 50, h - 300, width = 500, height = 250)
	text = c.beginText(50, h - 350)
	content = str(monitor.snmpConsult(target, '1.3.6.1.2.1.1.1.0'))
	if len(content) > 80:
		content = [content[:80], content[80:]]
		text.textLines('\n'.join(content))
	else:
		text.textLine(content)
	content = monitor.snmpConsult(target, '1.3.6.1.2.1.1.6.0')
	text.textLines(f'\n\nLocalizacion: {content}')

	content = monitor.snmpConsult(target, '1.3.6.1.2.1.2.1.0')
	text.textLines(f'\n\nNumero de interfaces: {content}')

	content = int(monitor.snmpConsult(target, '1.3.6.1.2.1.1.3.0'))/360000
	text.textLines(f'\n\nTiempo desde ultimo reinicio (horas): {content}')

	text.textLines(f'Comunidad: {monitor.comunity}')
	text.textLines(f'IP: {target}')

	text.setFont('Times-Roman', 12)
	c.drawText(text)
	c.showPage()

	inames = ['inunicast', 'inip', 'icmpecho', 'tcpsegsin', 'udpindtgr']
	c.drawString(w/2, h - 100, 'Graficas')
	pos = 300
	for iname in inames:

		c.drawImage(f'rrd/{target} {iname}.png', 50, h - pos, width = 500, height = 200)
		if pos == 780:
			c.showPage()
			pos = 300
		else:
			pos += 240
	c.save()

if __name__ == '__main__':
	from SNMPdata import MonitorInfo
	m = MonitorInfo(hosts = ['localhost'])
	tar = 'localhost'
	makeReport(m, tar)