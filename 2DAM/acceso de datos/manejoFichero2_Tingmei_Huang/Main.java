import java.io.*;
import java.util.HashMap;
import java.util.Map;


public class Main {
    public static void main(String[] args) {

        String fileName = "src/clientes";

         //cuantosRegistro(fileName);

         //cuantosCampo(fileName);

        //registroConMasCampo(fileName);

        // Contain1989(fileName);

         //cuantosCiempozuelo(fileName);

         ConvierteFicheroIndiceDNI(fileName);

       ConvierteFicheroIndiceApellido(fileName);


    }

    public static void cuantosRegistro(String fileName) {

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            int cont = 0;
            int character;
            // no entiendo
            while ((character = br.read()) != -1) {
                // si character es int
                if (character == '$') {
                    cont++;
                }
            }

            System.out.println("Cantidad de registro en el fichero cliente: " + (cont + 1)); //hay que sumar el último cliente

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void cuantosCampo(String fileName) {

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {

            String line;
            int register = 1;

            while ((line = br.readLine()) != null) {
                String[] persons = line.split("\\$");

                for (String person : persons) {
                    String values[] = person.split("#");
                    System.out.print(" Registro " + register + " :");
                    for (String value : values) {
                        System.out.print(value + " ,");
                    }
                    System.out.println();
                    register++;
                }
            }


        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    // solo he sacado uno de 5 campos , los demas son 6.
    public static void registroConMasCampo(String fileName) {

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            int register = 1;
            int registerLength = -1;

            while ((line = br.readLine()) != null) {
                String[] persons = line.split("\\$");

                for (String person : persons) {
                    String values[] = person.split("#");

                    if (registerLength == -1) {
                        registerLength = values.length;
                    } else if (registerLength != values.length) {
                        System.out.print("Registro " + register + ": ");
                        for (String value : values) {
                            System.out.print(value + ", ");
                        }
                        System.out.println();
                    }
                    register++;
                }
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void Contain1989(String fileName) {
        String line;
        int cont = 0;
        try {
            BufferedReader br = new BufferedReader(new FileReader(fileName));
            while ((line = br.readLine()) != null) {
                String persons[] = line.split("\\$");
                for (int i = 0; i < persons.length; i++) {
                    if (persons[i].contains("1989")) {
                        cont++;
                        // System.out.println(persons[i]);
                    }
                }
            }
            System.out.println("hay " + cont + " clientes nacieron en 1989 ");
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void cuantosCiempozuelo(String fileName) {
        String line;
        int cont = 0;

        try {
            BufferedReader br = new BufferedReader(new FileReader(fileName));
            while ((line = br.readLine()) != null) {
                String persons[] = line.split("\\$");
                for (String s : persons) {
                    if (s.contains("Ciempozuelos")) {
                        cont++;
                        //System.out.println(s);
                    }
                }
            }
            System.out.println("hay " + cont + " clientes viven en Ciempozuelos");
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void ConvierteFicheroIndiceDNI(String fileName) {

        Map<String, String> map = new HashMap<>();
        String line;
        String fileOutPut = "ficheroIndiceDni";

        try {
            BufferedReader br = new BufferedReader(new FileReader(fileName));

            while ((line = br.readLine()) != null) {
                String persons[] = line.split("\\$");

                for (int i = 0; i < persons.length; i++) {
                    String[] parts = persons[i].split("#", 2); // Dividir en dos parts usando '#' como delimitador

                    if (parts.length == 2) {
                        String key = parts[0];
                        String restParts = parts[1].replace("#", " ");

                        map.put(key, restParts);

                    }
                }

            }
            File outputFile = new File(fileOutPut);

            if (!outputFile.exists()) {
                outputFile.createNewFile();
            }

            BufferedWriter writer = new BufferedWriter(new FileWriter(fileOutPut));

            for (Map.Entry<String, String> entry : map.entrySet()) {
                String key = entry.getKey();
                String value = entry.getValue();
                writer.write(key + "#" + value);
                writer.newLine();
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void ConvierteFicheroIndiceApellido(String fileName) {
        Map<String, String> map = new HashMap<>();
        String line;
        String fileOutPut = "ficheroIndiceApellido";

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {

            while ((line = br.readLine()) != null) {
                String persons[] = line.split("\\$");

                for (int i = 0; i < persons.length; i++) {
                    String[] parts = persons[i].split("#");
                    String nameSurname = parts[1] + " " + parts[2];
                    String rest = "";
                    for ( int j = 0;j< parts.length;j++) {
                        if (j != 1 &&  j != 2 ) {
                            rest += parts[j]+" ";
                        }
                    }
                    map.put(nameSurname, rest);
                }

                File outputFile = new File(fileOutPut);

                if (!outputFile.exists()) {
                    outputFile.createNewFile();
                }

                BufferedWriter writer = new BufferedWriter(new FileWriter(fileOutPut));

                for (Map.Entry<String, String> entry : map.entrySet()) {
                    String key = entry.getKey();
                    String value = entry.getValue();
                    writer.write(key + "#" + value);
                    writer.newLine();
                }

            }

        } catch (FileNotFoundException ex) {
            throw new RuntimeException(ex);
        } catch (IOException ex) {
            throw new RuntimeException(ex);
        }
    }

}
