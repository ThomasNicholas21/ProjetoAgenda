# Passo a passo para primeiro Deploy VM
## VM
Uma Máquina Virtual (VM) é um ambiente de computação simulado que executa um sistema operacional e aplicativos como se fosse um computador físico. Ela é criada e gerenciada por um software chamado hypervisor, permitindo que vários sistemas operacionais rodem simultaneamente no mesmo hardware.
### **tipo de hypervisor**
Hypervisor é um software responsável por gerenciar as maquinas virtuais, permitindo compartilhar recursos do hardware físico. Sendo dividos em _bare metal_, que não necessita de um sistema operacional intermediário, e Hosted, que executa em um sistema operacional.

### Imagem VM
Uma __imagem__ normalmente contem um sistema operacional e configurações. Necessário baixar ISO do Ubunto.

### Virtualização, armazenamento e Snapshots
- Virtualização: A virtualização dos hardwares, permite que a VM tenha acesso de hardwares, podendo ser controlada pelo Hypervisor.