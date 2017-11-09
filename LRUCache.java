import java.util.LinkedHashMap;
import java.util.Map.Entry;

public class LRUCache extends LinkedHashMap {
    private static final long serialVersionUID = 1L;
    private final int capacity;
    private long accessCount = 0;
    private long hitCount = 0;

    public LRUCache(int capacity) {
    	super(capacity+1, 1.1f, true);
    	this.capacity = capacity;
    }

    public String get(String key) {
    	accessCount++;
    	if (super.containsKey(key)) {
    		hitCount++;
    	}
    	String value = (String)super.get(key);
    	return value;
    }
  	
  	public boolean containsKey(String key) {
  		accessCount++;
  		if (super.containsKey(key)) {
  			hitCount++;
  			return true;
  		} else {
  			return false;
  		}
  	}

  	protected boolean removeEldestEntry(Entry eldest) {
  		return size() > capacity;
  	}

  	public long getAccessCount() {
  		return accessCount;
  	}

  	public long getHitCount() {
  		return hitCount;
  	}
}
