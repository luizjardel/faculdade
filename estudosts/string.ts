function saudar(nome: string, titulo?: string) {
  return titulo ? '${titulo}`${nome}' : nome;
}
saudar("Ana");
saudar("Ana","Dra.")