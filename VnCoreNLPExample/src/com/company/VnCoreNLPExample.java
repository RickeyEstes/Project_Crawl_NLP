package com.company;

import vn.pipeline.*;
import java.io.*;
public class VnCoreNLPExample {
    /**
     * read content in file
     * @param filename: name of file
     * @return : String: content of file
     * @throws IOException
     */
    public static String readFile(String filename) throws IOException {
        StringBuffer sb = new StringBuffer();
        try {
            //file name is path to file
            File file = new File(filename);

            FileReader fr = new FileReader(file);   //reads the file
            BufferedReader br = new BufferedReader(fr);  //creates a buffering character input stream
                //constructs a string buffer with no characters
            String line;
            while ((line = br.readLine()) != null) {
                sb.append(line);      //appends line to string buffer
                sb.append("\n");     //line feed
            }
            fr.close();    //closes the stream and release the resource
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return sb.toString();
    }

    /**
     * get all name of file in a folder
     * @param pathFolder
     * @return:  array String: name of file
     */
    public static String[] getAllFileInFolder(String pathFolder) {
        File folder = new File(pathFolder);
        File[] listOfFiles = folder.listFiles();

        String [] arrFile = new String[listOfFiles.length];

        for (int i = 0; i < listOfFiles.length; i++) {
            if (listOfFiles[i].isFile()) {
                arrFile[i] = listOfFiles[i].getName();
            }
        }
        return arrFile;
    }
    public static void main(String[] args) throws IOException {
        String pathNameImport = "C:\\Users\\duclt\\PycharmProjects\\Crawler\\yte";
        String pathNameExport = "";
        // "wseg", "pos", "ner", and "parse" refer to as word segmentation, POS tagging, NER and dependency parsing, respectively.
        String[] annotators = {"wseg", "pos", "ner", "parse"};
        VnCoreNLP pipeline = new VnCoreNLP(annotators);
        String [] arrNameFile = getAllFileInFolder(pathNameImport);

        for(int i = 0; i < arrNameFile.length; i++) {
            String str = readFile(pathNameImport+"/"+arrNameFile[i]);

            Annotation annotation = new Annotation(str);
            pipeline.annotate(annotation);

//        System.out.println(annotation.toString());

            //Write to file
            // nếu muốn chỉ định thư mục out put thêm hàm xử lí tạo
            //PrintStream outputPrinter = new PrintStream(pathNameExport+"/"+arrNameFile[i]);
            PrintStream outputPrinter = new PrintStream("yte/"+arrNameFile[i]);
            pipeline.printToFile(annotation, outputPrinter);
        }
//        String str = readFile("a.txt");
//
//        Annotation annotation = new Annotation(str);
//        pipeline.annotate(annotation);
//
////        System.out.println(annotation.toString());
//
//        //Write to file
//        PrintStream outputPrinter = new PrintStream("output.txt");
//        pipeline.printToFile(annotation, outputPrinter);

        // You can also get a single sentence to analyze individually
//        Sentence firstSentence = annotation.getSentences().get(0);
//        System.out.println(firstSentence.toString());
    }
}