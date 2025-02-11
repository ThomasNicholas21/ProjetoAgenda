# Passo a passo para primeiro Deploy VM
## VM
Uma Máquina Virtual (VM) é um ambiente de computação simulado que executa um sistema operacional e aplicativos como se fosse um computador físico. Ela é criada e gerenciada por um software chamado hypervisor, permitindo que vários sistemas operacionais rodem simultaneamente no mesmo hardware.
### **tipo de hypervisor**
Hypervisor é um software responsável por gerenciar as maquinas virtuais, permitindo compartilhar recursos do hardware físico. Sendo dividos em _bare metal_, que não necessita de um sistema operacional intermediário, e Hosted, que executa em um sistema operacional.

### Imagem VM
Uma __imagem__ normalmente contem um sistema operacional e configurações. Necessário baixar ISO do Ubunto.

### Virtualização, armazenamento e Snapshots
- Virtualização: A virtualização dos hardwares, permite que a VM tenha acesso de hardwares, podendo ser controlada pelo Hypervisor.
- Armazenamento: A Vm utiliza discos virutal que simulam HD físicos.
- Snapshots: Forma de mostrar o estado atual da VM para que possa ser restaurada.

### Tipos de Virtualização
- **Virtualização Completa**
    - O hypervisor emula completamente o hardware para que o sistema operacional convidado funcione sem modificações.

- **Paravirtualização**
    - O SO convidado é modificado para se comunicar diretamente com o hypervisor, reduzindo a sobrecarga e aumentando a eficiência.

- **Virtualização de Armazenamento**
    - Permite abstrair diferentes dispositivos de armazenamento para as VMs, criando um pool de discos virtuais.

- **Virtualização de Rede**
    - Criação de redes virtuais dentro do hypervisor para isolar, conectar ou simular redes físicas.

- **Containers vs. VMs**
    - Os containers (exemplo: Docker, LXC) são uma forma de virtualização mais leve que compartilha o mesmo kernel do SO, diferente das VMs que possuem um SO completo.
