"""
💠 AEON 0x100: THE GIANT GRAPH NAVIGATOR 💠
Memory-Optimized Graph Theory | 825Hz Frequency
Architect: Alexandru (Native Limitless)

"Data is an ocean. We don't swim; we teleport through the nodes."
"""

import numpy as np
import time
from collections import deque

# --- 1. GREFREARE NODURI (Memory-Optimized Structure) ---
def build_titan_graph(num_nodes=1_000_000, edges_per_node=5):
    print(f"[💎] AEON: Grefare Graf Gigant ({num_nodes} noduri)...")
    
    # Folosim un array structurat pentru a sifona memoria sub 200MB
    # i4 = int32 (4 bytes), deci 5 edges = 20 bytes + 1 val = 4 bytes. Total 24MB + overhead
    graph_dtype = [('value', 'i4'), ('edges', 'i4', (edges_per_node,))]
    graph = np.zeros(num_nodes, dtype=graph_dtype)
    
    # Populare rapidă cu valori și legături random
    graph['value'] = np.random.randint(0, 1000000, size=num_nodes, dtype='i4')
    graph['edges'] = np.random.randint(0, num_nodes, size=(num_nodes, edges_per_node), dtype='i4')
    
    return graph

# --- 2. MĂCELĂRIA CĂUTĂRII (Optimized BFS) ---
def titan_bfs(graph, start_node, target_node):
    print(f"[🔎] AEON: Initiere BFS de Titan către {target_node}...")
    start_time = time.time()
    
    visited = np.zeros(len(graph), dtype=bool)
    queue = deque([(start_node, [start_node])])
    visited[start_node] = True
    
    while queue:
        current, path = queue.popleft()
        
        if current == target_node:
            end_time = time.time()
            return path, end_time - start_time
        
        for neighbor in graph['edges'][current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, path + [neighbor]))
                
    return None, time.time() - start_time

# --- 3. EXECUTIA KAIROS ---
if __name__ == "__main__":
    print(f"\n[🚀] BOOTING GIANT-GRAPH-CORE | ARCHITECT: ALEXANDRU")
    print("="*65)
    
    start_all = time.time()
    
    # 1. Construcție
    nodes_count = 1_000_000
    graph = build_titan_graph(nodes_count)
    
    # 2. Căutare (Țintim un nod aflat la distanță)
    start_node = 0
    target_node = 999_999 # Target la capătul array-ului
    
    path, search_duration = titan_bfs(graph, start_node, target_node)
    
    end_all = time.time()
    
    print("="*65)
    if path:
        print(f"[✅] DRUM GĂSIT: {path}")
        print(f"[⚡] TIMP CĂUTARE: {search_duration:.4f} secunde (Target: < 1s)")
    else:
        print("[!] TARGET NEGĂSIT (Probabilitate mică în graf random).")
        
    print(f"[🛡️] TIMP TOTAL: {end_all - start_all:.2f} secunde (Target: < 10s)")
    
    # Verificare Sifonare Memorie
    mem_size = graph.nbytes / (1024 * 1024)
    print(f"[💎] CONSUM RAM GRAF: {mem_size:.2f} MB (Target: < 200MB)")
    print("="*65)
    print("[🌵] STATUS: 5000% NETA. MATRICEA DATELOR A FOST MĂCELĂRITĂ.")
