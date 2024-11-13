# main.tf

# Usamos null_resource para ejecutar el script de Python solo una vez
resource "null_resource" "run_python_script" {
  # Ejecutamos el script de Python con local-exec
  provisioner "local-exec" {
    command = "py fibonacci.py"
  }
}

# Leemos el contenido del archivo "fibonacci.txt" generado por el script
data "local_file" "fibonacci" {
  filename = "${path.module}/fibonacci.txt"
  depends_on = [null_resource.run_python_script] # Asegura que el archivo se genere primero
}

# Output para mostrar la secuencia de Fibonacci
output "fibonacci_sequence" {
  value = data.local_file.fibonacci.content
}
