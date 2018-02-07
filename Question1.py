#I couldn't figure this question out

class Patient:
    '''master class'''
    def __init__(self, name):
        '''
        :param name: patient name
        '''
        self.name = name

    def discharge(self):
        '''abstract method to be overridden in derived classes'''
        raise NotImplemented("This is an abstract method and needs to be implemented in derived classes.")

class EmergencyPatient(Patient):

    def __init__(self, name, cost):
        '''
        :param name: patient name
        :param cost: discharge cost
               '''
        Patient.__init__(self, name)
        self.name=name
        self.cost=cost

    def discharge(self):
        '''return discharge cost of an Emergency patient'''


class HospitalizedPatient(Patient):

    def __init__(self, name, cost):
        '''

        :param name: patient name
        :param cost: cost
        '''
        Patient.__init__(self, name)
        self.name=name
        self.cost=cost

    def discharge(self):
        '''Return discharge cost of Hospitalized patient'''


class Hospital:
    def __init__(self, patient, cost):

        def admit(self, patient)
            self.patient.append(patient)


        def discharge_all()


        def get_total_cost

    myHospital = Hospital()

    Patient1=EmergencyPatient("a",1000)
    myHospital.admit(Patient1)

    Patient2=EmergencyPatient("b",1000)
    myHospital.admit(Patient2)

    Patient3=EmergencyPatient("c",1000)
    myHospital.admit(Patient3)

    Patient4=HospitalizedPatient("d",2000)
    myHospital.admit(Patient4)

    Patient5=HospitalizedPatient("e",2000)
    myHospital.admit(Patient5)


