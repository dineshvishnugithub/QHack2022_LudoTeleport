# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
import json

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, IBMQ, Aer
from qiskit.tools.monitor import job_monitor
import numpy as np
from numpy.random import randint

IBMQ.enable_account('ENTER API KEY HERE')
provider = IBMQ.get_provider(hub='ibm-q')

def home(request):
    return render(request, 'index.html', {})

def random(request):

    print(request.body)

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode);

    device = body['device']

    min = int(body['min'])
    max = int(body['max'])

    backend = provider.get_backend(device)

    if device == "ibmq_qasm_simulator":
        num_q = 32
    else:
        num_q = 5

    q = QuantumRegister(num_q, 'q')
    c = ClassicalRegister(num_q, 'c')

    circuit = QuantumCircuit(q, c)
    circuit.h(q)  # Applies hadamard gate to all qubits
    circuit.measure(q, c)  # Measures all qubits


    job = execute(circuit, backend, shots=1)

    print('Executing Job...\n')
    job_monitor(job)
    counts = job.result().get_counts()

    print('RESULT: ', counts, '\n')
    print('Press any key to close')

    result = int(counts.most_frequent(), 2)

    result1 = min + result % (max+1 - min)

    print(result1)

    response = JsonResponse({'result': result1})
    return response
def encode_message(bits, bases):
    message = []
    for i in range(n):
        qc = QuantumCircuit(1,1)
        # check if 0 then z basis else x bases
        if bases[i] == 0:
            if bits[i] == 0:
                pass
            else:
                qc.x(0)
        else:
            if bits[i] == 0:
                qc.h(0)
            else:
                qc.x(0)
                qc.h(0)
        qc.barrier()
        message.append(qc)
    return message    

def message_measured(message, bases):
    backend = Aer.get_backend('aer_simulator')
    measurements = []
    for q in range(n):
        if bases[q] == 0:
            message[q].measure(0,0)
        else:
            message[q].h(0)
            message[q].measure(0,0)
        ans = execute(message[q], backend = backend, shots = 1, memory = True).result()
        measured_bit = int(ans.get_memory()[0])
        measurements.append(measured_bit)
    return measurements

def remove_garbage(a_bases, b_bases, bits):
    good_bits = []
    for q in range(n):
        if a_bases[q] == b_bases[q]:
            good_bits.append(bits[q])
    return good_bits 

def sample_bits(bits, selection):
    sample = []
    for i in selection:
        i = np.mod(i, len(bits))
        sample.append(bits.pop(i))
    return sample    

def quantum_key_distribution(response):
    np.random.seed(seed = 0)
    n = response
    user_bits = randint(2, size = n)
    user_bases = randint(2, size = n)
    output_bases = randint(2, size = n) # for the output from the box
    message = encode_message(user_bits, user_bases)
    box_results = message_measured(message, output_bases) # result that we get from the box
    user_key = remove_garbage(user_bases, output_bases, user_bits)
    box_key = remove_garbage(user_bases, output_bases, box_results)
    sample_size = 2
    bit_selection = randint(n, size = sample_size)
    box_sample = sample_bits(box_key, bit_selection)
    user_sample = sample_bits(user_key, bit_selection)
    ans = user_sample[0] * 10 + user_sample[1]
    return ans
    
    