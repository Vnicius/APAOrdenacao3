def counting_sort(vetor):

	maior = vetor[0]

	#maior elemento
	for x in range(1,len(vetor)):
		if vetor[x] > maior:
			maior = vetor[x]

	count = [0] * (maior + 1)

	#contar ocorencias
	for x in vetor:
		count[x] += 1
	
	#calculo dos indices 
	for x in range(1,len(count)):
		count[x] += count[x-1]

	saida = [0] * len(vetor)

	#preenche array de saida
	for x in range(len(vetor)-1,-1,-1):
		saida[count[vetor[x]-1]] = vetor[x]
		count[vetor[x]-1] -= 1
	
	return saida


#####################################

def bucketSort(vetor):
	maior = vetor[0]

	#maior elemento
	for x in range(1,len(vetor)):
		if vetor[x] > maior:
			maior = vetor[x]

	buckets = [[]]
	saida = []
	x = 0
	#definir quantidade de buckets
	while x < int(maior/10):
		buckets.append([])
		x += 1
	
	#adicona os elementos aos buackets, ja de forma ordenada
	for num in vetor:
		aux = num
		if not buckets[int(aux/10)]:
			buckets[int(aux/10)].append(aux)
		else:
			for x in range(len(buckets[int(aux/10)])):
				if aux < buckets[int(aux/10)][x]:
					y = buckets[int(aux/10)][x]
					buckets[int(aux/10)][x] = aux
					aux = y
			buckets[int(num/10)].append(aux)

	return ([b for bucket in buckets for b in bucket])
	#return saida

###################################################
def radixSort(vetor):
	maior = vetor[0]

	#maior elemento
	for x in range(1,len(vetor)):
		if vetor[x] > maior:
			maior = vetor[x]

	exp = 1
	while maior/exp > 0:
		vetor = countingSortRadix(vetor,exp)
		exp *= 10
		#print vetor
	#print vetor

def countingSortRadix(vetor,exp):
	maior = vetor[0]

	#maior elemento
	for x in range(1,len(vetor)):
		if vetor[x] > maior:
			maior = vetor[x]

	count = [0] * (maior + 1)

	#contar ocorencias
	for x in vetor:
		count[(x/exp)%10] += 1
	
	#calculo dos indices 
	for x in range(1,len(count)):
		count[x] += count[x-1]

	saida = [0] * len(vetor)

	#preenche array de saida
	for x in range(len(vetor)-1,-1,-1):
		saida[count[(vetor[x]/exp)%10]-1] = vetor[x]
		count[(vetor[x]/exp)%10] -= 1
	
	return saida


###################################################

if __name__ == '__main__':
	vet = [1,2,5,12,9,4,6,100,102,99,39,13,12]
	radixSort(vet)
	print(bucketSort(vet))