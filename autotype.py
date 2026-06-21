import pyautogui
import time

def wpm_to_char_delay(wpm):
    """
    Converts words per minute (WPM) to a delay per character.
    
    :param wpm: Typing speed in words per minute.
    :return: Delay between characters in seconds.
    """
    return 60 / (wpm * 5)

def auto_type(text, wpm, line_delay=0.5):
    """
    Simulates typing the given text with a delay based on the typing speed (WPM) and between each line.
    Ignores leading spaces in each new line.
    
    :param text: The string to type.
    :param wpm: Typing speed in words per minute.
    :param line_delay: The delay between typing each line in seconds.
    """
    char_delay = wpm_to_char_delay(wpm)  # Calculate the delay per character based on WPM
    lines = text.split('\n')  # Split the text by lines
    
    for line in lines:
        line = line.lstrip()  # Remove leading spaces from the line
        pyautogui.write(line, interval=char_delay)  # Type the line with appropriate delay between characters
        pyautogui.press('enter')  # Simulate pressing Enter key for new lines
        time.sleep(line_delay)  # Wait before typing the next line

if __name__ == "__main__":

    # Customize the text and typing speed
    text_to_type = ''' import java.util.Scanner;

public class Main {
    int V;
    int[] path;
    int[][] graph;

    public Main(int[][] graph) {
        this.V = graph.length;
        this.graph = graph;
        this.path = new int[V];
    }

    boolean isSafe(int v, int pos) {
        if (graph[path[pos - 1]][v] == 0) return false;
        for (int i = 0; i < pos; i++) if (path[i] == v) return false;
        return true;
    }

    boolean hamiltonianCycleUtil(int pos) {
        if (pos == V) return graph[path[pos - 1]][path[0]] == 1;
        for (int v = 1; v < V; v++) {
            if (isSafe(v, pos)) {
                path[pos] = v;
                if (hamiltonianCycleUtil(pos + 1)) return true;
                path[pos] = -1;
            }
        }
        return false;
    }

    void hamiltonianCycle() {
        path[0] = 0;
        for (int i = 1; i < V; i++) path[i] = -1;
        if (hamiltonianCycleUtil(1)) {
            for (int i = 0; i < V; i++) System.out.print(path[i]);
            System.out.println(0);
        } else System.out.println("Hamiltonian Cycle not found");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int V = scanner.nextInt();
        int[][] graph = new int[V][V];
        for (int i = 0; i < V; i++)
            for (int j = 0; j < V; j++)
                graph[i][j] = scanner.nextInt();
        Main hc = new Main(graph);
        hc.hamiltonianCycle();
        scanner.close();
    }
}
;


'''

    wpm = 60  # Set the typing speed here in WPM
    line_delay = 1.5  # Adjust the delay between lines here

    print("Typing will start in 3 seconds...")
    time.sleep(3)  # Delay to switch focus to a text input field
    auto_type(text_to_type, wpm, line_delay)
