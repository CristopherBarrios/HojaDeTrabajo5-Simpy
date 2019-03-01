##
##  Luis Pedro Cuellar - 18220
##  Cristopher Barrios -
##  Fecha: 2/28/2019
##  Simulation.py
##
##  Programa que se encarga en hacer procesos usando el "ram" y el "procesador"

import simpy
import random

print(" ")
print(" --- SIMULACION DE SISTEMA OPERATIVO --- ")

randomSeed = 50
time = []
interval = 10
total = 0

qtyProcesors = int(input(" Ingrese la cantidad de procesadores que desea tener: "))
qtyProcesses = int(input(" Ingrese la cantidad de procesos que desea hacer: "))

class OS(object):
    def __int__(self, env, qtyProcesses, mmry):
        self.env = env
        self.CPU = simpy.Resource(env, capacity=qtyProcesors)
        self.RAM = simpy.Container(env, mmry, init=0)
        self.qtyProcesses = qtyProcesses

    def addRAM(self, mmry):
        if(self.RAM.capacity - self.RAM.level) < mmry:
            self.RAM.put(mmry)

class Process(object):
    def __int__(self, env, instructions, ex, RAMpp, simulation, name, inicio):
        self.env = env
        self.action = env.process(self.run(env, ex, RAMpp, simulation, name, inicio))
        self.instructions = instructions


    def run(self, env, ex, RAMpp, simulation, name, inicio):
        yield env.timeout(2)
        instructionCont = 3

        with simulation.cpu.request()  as requested:
            while interval == 10:
                try:
                    instructionCont -= 1
                    yield self.env.timeout(ex)
                    yield requested

                except simpy.Interrupt:
                    if self.instructions < 0:
                        env.process(finish(env, RAMpp, simulation, name, inicio))


def Proceso(processName, env, total):
    mmry = random.randint(1,10)
    inst = random.randint(1, 10)

    requested = new.request()
    yield requested

    print("<MMRY> Pidiendo memoria en t = " + str(int(env.now)))
    if mmry < RAM.level:
        RAM.get(mmry)
        new.release(requested)
        print("> RAM level: " + str(RAM.level))

    else:
        print("< No hay suficiente memoria")

    print("<CPU> Pidiendo acceso a CPU en t= " + str(int(env.now)))

def generateProcess(env, total, num1, interval):
    for i in range (num1):
        processName = "Peoceso" + str(i + 1)
        p = proceso(processName, env, total)
        env.process(p)
        t = random.expovariate(1/interval)
        yield env.timeout(t)

random.seed(randomSeed)
env = simpy.Environment
RAM = simpy.Container(env, init=0, capacity=100)
new = simpy.Resource(env, capacity=qtyProcesses)
CPU = simpy.Resource(env, capacity=qtyProcesors)
IO = simpy.Resource(env, capacity=2)
env.process(generateProcess(env, total, qtyProcesses, interval))
env.run()








